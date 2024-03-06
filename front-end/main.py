import flet as ft


def main(page: ft.Page):
    page.title = "CupertinoNavigationBar Example"
    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=ft.colors.WHITE,
        inactive_color=ft.colors.BLACK,
        active_color=ft.colors.GREEN_ACCENT_700,
        on_change=lambda e: print("Selected tab:", e.control.selected_index),
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Inicio"),
            ft.NavigationDestination(
                icon=ft.icons.SCHEDULE_SEND_ROUNDED, label="Programar"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Explore",
            ),
        ]
    )

    page.add(
        # ft.Container(
        #     ft.Card(
        #         content=ft.Container(
        #             content=ft.Column(
        #                 [
        #                     ft.ListTile(
        #                         leading=ft.Icon(ft.icons.ALBUM),
        #                         title=ft.Text("The Enchanted Nightingale"),
        #                         subtitle=ft.Text(
        #                             "Music by Julie Gable. Lyrics by Sidney Stein."
        #                         ),
        #                     ),
        #                     ft.Row(
        #                         [ft.TextButton("Buy tickets"), ft.TextButton("Listen")],
        #                         alignment=ft.MainAxisAlignment.END,
        #                     ),
        #                 ]
        #             ),
        #             width=400,
        #             padding=10,
        #         )
        #     )
        # ),
        ft.Card(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.ListTile(
                                            leading=ft.Icon(ft.icons.ALBUM),
                                            title=ft.Text(
                                                "Titulo",
                                                color=ft.colors.BLACK
                                            ),
                                            subtitle=ft.Text(
                                                "Music by Julie Gable. Lyrics by Sidney Stein.",
                                                color=ft.colors.GREY
                                            ),
                                        ),
                                        ft.Row(
                                            [ft.TextButton("Buy tickets"),
                                             ft.TextButton("Listen")],
                                            alignment=ft.MainAxisAlignment.END,
                                        ),
                                    ],
                                ),
                                margin=10,
                                padding=10,
                                alignment=ft.alignment.top_left,
                                bgcolor=ft.colors.GREEN_ACCENT_200,
                                width=1000,
                                height=150,
                                border_radius=10,
                                ink=True,
                                on_click=lambda e: print(
                                    "Clickable with Ink clicked!"),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ), ft.Row(
                        [
                            ft.Container(
                                content=ft.Column(
                                    [
                                        ft.ListTile(
                                            leading=ft.Icon(ft.icons.ALBUM),
                                            title=ft.Text(
                                                "Titulo",
                                                color=ft.colors.BLACK
                                            ),
                                            subtitle=ft.Text(
                                                "Music by Julie Gable. Lyrics by Sidney Stein.",
                                                color=ft.colors.GREY
                                            ),
                                        ),
                                        ft.Row(
                                            [ft.TextButton("Buy tickets"),
                                             ft.TextButton("Listen")],
                                            alignment=ft.MainAxisAlignment.END,
                                        ),
                                    ],
                                ),
                                margin=10,
                                padding=10,
                                alignment=ft.alignment.top_left,
                                bgcolor=ft.colors.GREEN_ACCENT_200,
                                width=1000,
                                height=150,
                                border_radius=10,
                                ink=True,
                                on_click=lambda e: print(
                                    "Clickable with Ink clicked!"),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                ]
            ),
            color=ft.colors.WHITE,
        ),
    )


ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
