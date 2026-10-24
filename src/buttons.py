import discord

class VistaButton(discord.ui.View):
    def __init__(self, play_func):
        self.play_func = play_func  # Función real que reproduce el sonido
        super().__init__()

    @discord.ui.button(label="Fireball", style=discord.ButtonStyle.green)
    async def sound1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 1)
        #await interaction.response.send_message(f" Reproducido con exito", ephemeral=True)
        await interaction.response.defer(ephemeral=True)
    
    @discord.ui.button(label="Llamarada", style=discord.ButtonStyle.green)
    async def sound7(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 7)
        await interaction.response.defer(ephemeral=True)

    @discord.ui.button(label="Llamarada XXL", style=discord.ButtonStyle.green)
    async def sound8(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 8)
        await interaction.response.defer(ephemeral=True)
    
    @discord.ui.button(label="Spell", style=discord.ButtonStyle.green)
    async def sound13(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 13)
        await interaction.response.defer(ephemeral=True)

    @discord.ui.button(label="Thunershoot", style=discord.ButtonStyle.green)
    async def sound2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 2)
        await interaction.response.defer(ephemeral=True)

    @discord.ui.button(label="Drink", style=discord.ButtonStyle.green)
    async def sound3(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 3)
        await interaction.response.defer(ephemeral=True)
    
    @discord.ui.button(label="Cast", style=discord.ButtonStyle.green)
    async def sound4(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 4)
        await interaction.response.defer(ephemeral=True)

    @discord.ui.button(label="Crow", style=discord.ButtonStyle.green)
    async def sound5(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 5)
        await interaction.response.defer(ephemeral=True)

    @discord.ui.button(label="Wolf", style=discord.ButtonStyle.green)
    async def sound14(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 14)
        await interaction.response.defer(ephemeral=True)
    
    @discord.ui.button(label="Bear", style=discord.ButtonStyle.green)
    async def sound16(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 16)
        await interaction.response.defer(ephemeral=True)
    
    @discord.ui.button(label="Espada", style=discord.ButtonStyle.green)
    async def sound6(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 6)
        await interaction.response.defer(ephemeral=True)

    @discord.ui.button(label="Espada 2", style=discord.ButtonStyle.green)
    async def sound10(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 10)
        await interaction.response.defer(ephemeral=True)
    
    @discord.ui.button(label="Martillo", style=discord.ButtonStyle.green)
    async def sound11(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 11)
        await interaction.response.defer(ephemeral=True)
      
    @discord.ui.button(label="Flecha", style=discord.ButtonStyle.green)
    async def sound15(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 15)
        await interaction.response.defer(ephemeral=True)

    @discord.ui.button(label="Monster CRY", style=discord.ButtonStyle.red)
    async def sound12(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 12)
        await interaction.response.defer(ephemeral=True)

    @discord.ui.button(label="Plaza Pueblo", style=discord.ButtonStyle.red)
    async def sound9(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.play_func(interaction, 9)
        await interaction.response.defer(ephemeral=True)

        