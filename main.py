import os

import flet
from flet import Card, ElevatedButton, LoginEvent, Page, Column, Alignment, Container
from flet.auth.providers import GitHubOAuthProvider, GoogleOAuthProvider

GOOGLE_CLIENT_ID="xxx"
GOOGLE_CLIENT_SECRET="xxx"

GITHUB_CLIENT_ID="xxx"
GITHUB_CLIENT_SECRET="xxx"

REDIRECT_URL="http://127.0.0.1:8550/api/oauth/redirect"

def main(page: Page):
    
    texto_login = flet.Text()
    
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    
    google_provider = GoogleOAuthProvider(
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        redirect_url=REDIRECT_URL,
    )
    
    github_provider = GitHubOAuthProvider(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_url=REDIRECT_URL,
    )

    def login_google_button_click(e):
        page.login(google_provider)

    def login_github_button_click(e):
        page.login(github_provider, scope=["public_repo"])

    def on_login(e: LoginEvent):
        user_name = page.auth.user['name'] or ''
        print(page.auth.user)
        texto_login.value = 'Bienvenido/a {}'.format(user_name)
        page.update()
        if not e.error:
            print('ERROR DETECTADO: {}'.format(e))
            toggle_login_buttons()

    def logout_button_click(e):
        page.logout()

    def on_logout(e):
        toggle_login_buttons()

    def toggle_login_buttons():
        login_github_button.visible = page.auth is None
        login_google_button.visible = page.auth is None
        logout_button.visible = page.auth is not None
        texto_login.value = ''
        page.update()

    login_google_button = ElevatedButton("Login with Google", on_click=login_google_button_click)
    login_github_button = ElevatedButton("Login with GitHub", on_click=login_github_button_click)
    
    logout_button = ElevatedButton("Logout", on_click=logout_button_click)
    
    page.appbar = flet.AppBar(
        leading=flet.Icon(flet.icons.PALETTE),
        leading_width=40,
        title=texto_login,
        center_title=False,
        bgcolor=flet.colors.SURFACE_VARIANT,
        actions=[
            # flet.IconButton(flet.icons.WB_SUNNY_OUTLINED),
            # flet.IconButton(flet.icons.FILTER_3),
            flet.PopupMenuButton(
                items=[
                    flet.PopupMenuItem(),
                    flet.PopupMenuItem(
                        text="Google Login",
                        on_click=login_google_button_click
                    ),
                    flet.PopupMenuItem(
                        text="Github Login",
                        on_click=login_github_button_click
                    ),
                    flet.PopupMenuItem(
                        text="Logout",
                        on_click=logout_button_click,
                        
                    )
                ]
            ),
        ],
    )
    
    
    toggle_login_buttons()
    
    page.on_login = on_login
    page.on_logout = on_logout
    
    # page.add(
    #     Card(
    #         content=Container(
    #             content=Column(
    #                 [
    #                     login_google_button,
    #                     login_github_button,
    #                     logout_button
    #                 ]
    #             ),
    #             alignment=flet.alignment.center,
    #             padding=10,
    #             border_radius=8,
    #             bgcolor="white"
    #         )
    #     )
    # )

flet.app(target=main, port=8550, view=flet.WEB_BROWSER)