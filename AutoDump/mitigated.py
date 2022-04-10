from dhooks import Webhook, Embed

embed = Embed(
        description='**Attack has ended for:**\n``VeteranVPN Canada OVH-GAME``\n\n**Server Provider:**\n``OVH Hosting``\n\n**Location:**\n``Canada, US``\n\n**Attack successfully mitigated the OVH has been withdrawn from the mitgation infrastructure**',
        color=0xfafcfa,
        timestamp='now'
        )

embed.set_thumbnail('https://www.seekpng.com/png/full/205-2059350_safe-black-and-white-verified.png')
embed.set_footer(text="Attack Mitigated")

hook = Webhook('https://canary.discord.com/api/webhooks/944698101506121788/5-20_5tXrKrS0zD76MNxwGXndsU7kt-ire6EY7M2CboweCTvAlPrIoLouTr5NBGlDeMN')

hook.send(embed=embed)
