from dhooks import Webhook, Embed

embed = Embed(
        title='OVH-1',
        url='https://felixvpn.co.uk/',
        description='**Attack has been detected for:**\n``Canada OVH-GAME``\n\n**ISP:**\n``OVH Hosting``\n\n**RDNS:**\n``ovh-game-1.ovh``\n\n**Location:**\n``Canada, US``\n\n**Attack is currently being filtered via OVH VAC**',
        color=0x00bbff,#=blue
        timestamp='now'
        )

embed.set_thumbnail('https://icons555.com/images/icons-red/image_icon_warning_3_pic_512x512.png')

embed.set_image('https://bestanimations.com/Flags/Canada/canada-flag-animated-gif-11.gif')

embed.set_footer(text="Attack Detected")

hook = Webhook('https://canary.discord.com/api/webhooks/944698101506121788/5-20_5tXrKrS0zD76MNxwGXndsU7kt-ire6EY7M2CboweCTvAlPrIoLouTr5NBGlDeMN')

hook.send(embed=embed)
