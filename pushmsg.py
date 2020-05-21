import pusher

pusher_client = pusher.Pusher(
    app_id="1005328",
    key="532b456bec622945e703",
    secret="7431854923c1fa75ad82",
    cluster="ap3",
    ssl=True,
)


def send_msg(user_name):
    pusher_client.trigger("all-channel", user_name, {"message": "hello world"})
