from py2html import tag


head = tag.Head(
    children=[
        tag.Link(
            href="https://fonts.googleapis.com/css?family=Open+Sans:700,300", 
            rel="stylesheet",
            type="text/css"
        ),
        tag.Link(
            href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css", 
            rel="stylesheet",
            type="text/css"
        ),
        tag.Style(text='''.align-center {
    text-align: center;
}
body {
  background-color: #35415c;
}
h1 {
  font-family: "Open Sans";
  font-weight: 300;
  color: white;
}
h1 b {
  font-weight: 700;
}
.fa {
  padding-left: 20px;
  padding-right: 20px;
  padding-top: 50px;
}
.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  margin-left: -127px;
  margin-top: -84px;
  width: 290px;
  height: 168px;
}
.bi::before {
  font-size: 30px;
  color: white;
  padding: 20px;
}'''
        ),
        tag.Title("Felipe Ruhland"),
    ]
)
body = tag.Body(
    children=[
        tag.Div(
            children=[
                tag.Div(
                    children=[
                        tag.H1(text=f'FELIPE{tag.B("RUHLAND").render()}')
                    ],**{"class": "align-center"}
                ),
                tag.Div(
                    children=[
                        tag.A(
                            href="https://github.com/feliperuhland",
                            children=[
                                tag.I(**{"class": "bi bi-github"})
                            ],
                        ),
                        tag.A(
                            href="https://br.linkedin.com/in/feliperuhland",
                            children=[
                                tag.I(**{"class": "bi bi-linkedin"})
                            ],
                        ),
                        tag.A(
                            href="https://gitlab.com/feliperuhland",
                            children=[
                                tag.I(**{"class": "bi bi-gitlab"})
                            ],
                        ),
                        tag.A(
                            href="https://stackoverflow.com/users/2348371/feliperuhland",
                            children=[
                                tag.I(**{"class": "bi bi-stack-overflow"})
                            ],
                        )
                    ],**{"class": "align-center"}
                ),
            ],
            **{"class": "centered"}
        )
    ]
)


doc = tag.Document(
    children=[
        tag.Doctype(),
        head,
        body
    ]
)

print(doc.render())
