from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from organizations import models as organization_model


class LoggedInOnlyView(LoginRequiredMixin):

    login_url = reverse_lazy("user:login")


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return redirect("core:core")


class VerifiedUserOnlyView(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.email_verified is True

    def handle_no_permission(self):
        messages.error(self.request, "이메일 인증 후 사용 가능합니다")
        return redirect("core:core")


class MasterUserOnlyView(UserPassesTestMixin):
    def test_func(self):
        master = organization_model.Organization.objects.filter(
            master=self.request.user
        )
        if len(master) == 0:
            return False
        else:
            return True

    def handle_no_permission(self):
        messages.error(self.request, "그룹 관리자만 이용 가능합니다")
        return redirect("core:core")
