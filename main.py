from fasthtml.common import *
from fasthtml.svg import *

card_datas=[{'title':'Data extraction from Engineering Drawing',
             'info':'We developed a pipeline that includes symbol detection to extract relevant numerical data such as radius, diameter, roughness, etc from the given image of Engineering Drawing. The extracted information is then presented in tabular format.'
             },
            {'title':'Image to 3d Reconstruction project',
             'info':'Developed a tool that ingests reference data from multiple viewpoints, including left, right, top, bottom, front, and back, for a given target mesh. Using this reference data, the tool reconstructed the textured mesh that can be exported in mesh format'},
            {'title':'Dysarthria speech project with Voice cloning feature',
             'info':"""Created a tool that helps people suffering from Speech problems. This tool was made for clients who had speech issues. This tool takes a person's speech as input, the tool evaluates what the person is speaking and returns clear audio in his voice"""},
            {'title':'Voice generation and modulation tools project',
             'info':"""In this project, we harnessed cutting-edge technologies to create a suite of advanced tools. The Text-to-Speech system we developed produces remarkably human-like speech. For Speech-to-Text, we trained a custom model to transcribe Marathi, a language that previously lacked robust STT support. Our voice conversion techniques transform one speaker's voice to sound like another's, while our voice cloning system replicates not only a person’s voice but also their unique conversational style. Additionally, we leveraged AI to generate context-specific background music and high-quality sound effects. It's a comprehensive blend of innovation in voice and sound technology!"""},
            {'title':'Human position tracking ',
             'info':'As part of an iOS app project, we implemented a guidance feature that assists users in positioning themselves correctly in front of the camera. Leveraging YOLO v8’s bounding box and human body feature points, we fine-tuned the YOLO v8 model to align with our specific use case. The resulting model was successfully deployed within the iOS application.'},
            {'title':'Point Cloud Data classification',
             'info':'Developed a PCD rating feature as part of the same project. Leveraging PointNet, we analyzed input PCD (Point Cloud Data) values, making decisions based on their condition. The system categorized PCD into three outcomes: good, bad, or invalid. Additionally, I successfully deployed this feature within the same iOS application'},
            ]

cards=[]
for i,data in enumerate(card_datas):
    data = Div(
        Div(
            Div(data['title'],
                cls='header',
                style="""padding: 5% 5% 5% 5%;
                font-weight: 400; 
                        font-size: larger;"""),
            cls='centered'
        ),
        # Div(
        #     Image(src="OIP (3).jpeg")
        #     ),
        Div(
            data['info'],
            cls='details centered',
            style="""padding: 5% 5% 5% 5%;
                    font-size: medium;"""
                    
            ),
        style="""
        height: 400px;
                background-color: #3e4b50;
                border-radius: 10px;
                margin: 10px;
        """,
        cls='slider-item equal-height style-6'
    )
    cards.append(data)




app, rt = fast_app(live=True)

# print(picolink)
# app = FastHTML()

linkedinurl = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iMWVtIiB2aWV3Qm94PSIwIDAgMjQgMjQiPjxwYXRoIGZpbGw9IndoaXRlIiBkPSJNMjAuNDcgMkgzLjUzYTEuNDUgMS40NSAwIDAgMC0xLjQ3IDEuNDN2MTcuMTRBMS40NSAxLjQ1IDAgMCAwIDMuNTMgMjJoMTYuOTRhMS40NSAxLjQ1IDAgMCAwIDEuNDctMS40M1YzLjQzQTEuNDUgMS40NSAwIDAgMCAyMC40NyAyTTguMDkgMTguNzRoLTN2LTloM1pNNi41OSA4LjQ4YTEuNTYgMS41NiAwIDEgMSAwLTMuMTJhMS41NyAxLjU3IDAgMSAxIDAgMy4xMm0xMi4zMiAxMC4yNmgtM3YtNC44M2MwLTEuMjEtLjQzLTItMS41Mi0yQTEuNjUgMS42NSAwIDAgMCAxMi44NSAxM2EyIDIgMCAwIDAtLjEuNzN2NWgtM3YtOWgzVjExYTMgMyAwIDAgMSAyLjcxLTEuNWMyIDAgMy40NSAxLjI5IDMuNDUgNC4wNloiLz48L3N2Zz4="
hfurl = "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxZW0iIGhlaWdodD0iMWVtIiB2aWV3Qm94PSIwIDAgMjQgMjQiPjxwYXRoIGZpbGw9IiNlZWI4NmQiIGQ9Ik0xLjQ0NSAxMS41MDZjMCAxLjEwMi4xNjcgMi4xNTguNDg0IDMuMTU2Yy0uMDM4LS4wMDMtLjA2OS0uMDA2LS4xMDYtLjAwNmMtLjQyIDAtLjgwMS4xNi0xLjA3LjQ1MmMtLjM0NS4zNzMtLjQ5OC44MzMtLjQzMSAxLjI5M2ExLjYgMS42IDAgMCAwIC4yMTQuNTk3YTEuNDMgMS40MyAwIDAgMC0uNDg0Ljc1OGMtLjA2NS4yNDUtLjEzMS43NTQuMjE1IDEuMjhsLS4wNjMuMTA1Yy0uMjA4LjM5Mi0uMjIuODM3LS4wMzcgMS4yNWMuMjc5LjYyNi45NyAxLjExOCAyLjMxMyAxLjY0N2MuODM1LjMyOSAxLjU5OS41NCAxLjYwNS41NDNjMS4xMDUuMjg0IDIuMTA0LjQyNyAyLjk3LjQyN2MxLjQxNyAwIDIuNDc1LS4zODQgMy4xNTItMS4xNDRjMS41MzguMjY1IDIuNzkuMTQgMy41OTIuMDA2Yy42NzcuNzU1IDEuNzMzIDEuMTM5IDMuMTQ3IDEuMTM5Yy44NjQgMCAxLjg2NC0uMTQzIDIuOTY5LS40MjhjLjAwNi0uMDAyLjc3LS4yMTQgMS42MDUtLjU0M2MxLjM0My0uNTMgMi4wMzQtMS4wMjEgMi4zMTMtMS42NDdhMS40IDEuNCAwIDAgMC0uMDM3LTEuMjVsLS4wNjMtLjEwNWMuMzQ2LS41MjUuMjgtMS4wMzUuMjE1LTEuMjhhMS40MyAxLjQzIDAgMCAwLS40ODQtLjc1OHEuMTY2LS4yNy4yMTUtLjU5N2MuMDY2LS40Ni0uMDg3LS45Mi0uNDMyLTEuMjkzYTEuNDMgMS40MyAwIDAgMC0xLjA3LS40NTJsLS4wNi4wMDJhMTAuNCAxMC40IDAgMCAwIC40ODUtMy4xNTJjMC01LjgwNy00LjczNi0xMC41MTQtMTAuNTc5LTEwLjUxNGMtNS44NDIgMC0xMC41NzggNC43MDctMTAuNTc4IDEwLjUxNG0xMC41NzgtOS40ODNjNS4yNzMgMCA5LjU0OCA0LjI0NiA5LjU0OCA5LjQ4M2E5LjQgOS40IDAgMCAxLS4yNyAyLjIzNmwtLjAxMS0uMDE1YTEuNDIgMS40MiAwIDAgMC0xLjEwOC0uNTA2Yy0uMzUyIDAtLjcxNC4xMTUtMS4wNzYuMzQ0Yy0uMjQuMTUxLS41MDYuNDIyLS43OC43NmMtLjI1My0uMzUtLjYwNy0uNTg0LTEuMDEzLS42NDdhMS41IDEuNSAwIDAgMC0uMjM1LS4wMThjLS45MjYgMC0xLjQ4Mi44LTEuNjkzIDEuNTE4Yy0uMTA1LjI0My0uNjA3IDEuMzQ4LTEuMzYxIDIuMDk4Yy0xLjE2OSAxLjE2LTEuNDQ2IDIuMzUzLS44NCAzLjYzOGE5LjMgOS4zIDAgMCAxLTIuMzY1LS4wMDZjLjU5LTEuMjEyLjM2My0yLjQzOS0uODQzLTMuNjMyYy0uNzU1LS43NS0xLjI1Ni0xLjg1NS0xLjM2MS0yLjA5OGMtLjIxLS43MTgtLjc2Ny0xLjUxOC0xLjY5NC0xLjUxOHEtLjExNyAwLS4yMzQuMDE4Yy0uNDA2LjA2My0uNzYuMjk3LTEuMDE0LjY0NmMtLjI3My0uMzM3LS41MzktLjYwOC0uNzc5LS43NmMtLjM2Mi0uMjI4LS43MjQtLjM0My0xLjA3Ni0uMzQzYy0uNDI3IDAtLjgxLjE3LTEuMDgyLjQ3OGE5LjQgOS40IDAgMCAxLS4yNi0yLjE5M2MwLTUuMjM3IDQuMjc1LTkuNDgzIDkuNTQ3LTkuNDgzbS0zLjM3OSA0Ljk4YTEuMzYgMS4zNiAwIDAgMC0uNjI5IDIuNTYzYy4zNTEuMTg2LjQ4OS0uNTI2LjgzNi0uNjQ4Yy4zMTEtLjExLjg0MS4zOTkgMS4wMDguMDg2YTEuMzYgMS4zNiAwIDAgMC0uNTYyLTEuODRhMS40IDEuNCAwIDAgMC0uNjUzLS4xNm02Ljg0IDBhMS4zNiAxLjM2IDAgMCAwLTEuMjE1IDJjLjE2OC4zMTQuNjk4LS4xOTUgMS4wMDktLjA4NWMuMzQ3LjEyMi40ODYuODM1LjgzOC42NDhhMS4zNiAxLjM2IDAgMCAwIC41NjItMS44NGExLjM3IDEuMzcgMCAwIDAtMS4xOTMtLjcyMk01LjcyOSA4LjQyM2EuODc3Ljg3NyAwIDAgMC0uODc3Ljg3N2MwIC40ODQuMzkzLjg3Ny44NzcuODc3YS44NzcuODc3IDAgMCAwIC44NzctLjg3N2EuODc3Ljg3NyAwIDAgMC0uODc3LS44NzdtMTIuNjQ0IDBhLjg4Ljg4IDAgMCAwLS44OC44NzdhLjg4Ljg4IDAgMCAwIC44OC44NzdhLjg3Ny44NzcgMCAwIDAgLjg3Ni0uODc3YS44NzcuODc3IDAgMCAwLS44NzctLjg3N20tOS41OCAzLjAzN2MtLjE3OC0uMDAzLS4yNzkuMTEtLjI3OS40MTZjMCAuODEuMzg4IDIuMTI1IDEuNDI4IDIuOTI0Yy4yMDctLjcxMiAxLjM0Ni0xLjI4MyAxLjUwOC0xLjIwMWMuMjMyLjExNi4yMi40NDEuNjA4LjcyNmMuMzg4LS4yODUuMzc0LS42MS42MDUtLjcyNmMuMTYzLS4wODIgMS4zMDEuNDg5IDEuNTA4IDEuMjAxYzEuMDQtLjc5OSAxLjQyOC0yLjExNCAxLjQyOC0yLjkyNGMwLTEuMjIxLTEuNTgzLjY0LTMuNTQxLjY0OWMtMS40NjktLjAwNy0yLjcyNy0xLjA1Ni0zLjI2NC0xLjA2NW0tNC40OCAzLjAxOGMuNTguMzY1IDEuNjk2IDIuMjc1IDIuMTA2IDMuMDE4YS42Ni42NiAwIDAgMCAuNTgyLjM1M2MuNDE4IDAgLjc0Ni0uNDE0LjAzOS0uOTRjLTEuMDY0LS43OS0uNjkyLTIuMDg0LS4xODQtMi4xNjRhLjQuNCAwIDAgMSAuMDY2LS4wMDRjLjQ2MiAwIC42NjYuNzkuNjY2Ljc5cy41OTYgMS40OSAxLjYyMiAyLjUwOGMuOTQyLjkzNSAxLjA2MiAxLjcwMy40OTYgMi42NjZjLS4wMTYtLjAwNC0uMDE2LjAyMy0uMTQ4LjIxNWExLjkgMS45IDAgMCAxLS43Mi42MTVjLS41MDUuMjI3LTEuMTM5LjI3LTEuNzgzLjI3YTExLjggMTEuOCAwIDAgMS0yLjY5Ny0uMzM3Yy0uMDMtLjAwNy0zLjY1LS45NTYtMy4xOTItMS44MjJjLjA3Ny0uMTQ1LjIwNC0uMjAzLjM2NC0uMjAzYy42NDYgMCAxLjgyMy45NTUgMi4zMjguOTU1Yy4xMTMgMCAuMTk2LS4wODYuMjI4LS4yMDNjLjIyNS0uODA1LTMuMjc4LTEuMDUyLTIuOTg0LTIuMTY0Yy4wNTItLjE5Ny4xOTMtLjI3Ni4zOS0uMjc2Yy44NTQgMCAyLjc3IDEuNDkzIDMuMTczIDEuNDkzcS4wNDYgMCAuMDY0LS4wMjhjLjIwMS0uMzIyLjExLS41ODYtMS4zMDktMS40NGMtMS40MTgtLjg1My0yLjQzMS0xLjMyOC0xLjg2NS0xLjk0Yy4wNjUtLjA3Mi4xNTctLjEwMi4yNy0uMTAyYy44NiAwIDIuODk0IDEuODQgMi44OTQgMS44NHMuNTQ5LjU2OC44ODEuNTY4YS4yLjIgMCAwIDAgLjE4Ni0uMTA1Yy4yMzUtLjM5NS0yLjE4Ni0yLjIxOS0yLjMyMy0yLjk3MWMtLjA5Mi0uNTEuMDY0LS43NjguMzU2LS43NjhjMCAuMDA4LjE3LS4wMjkuNDk0LjE3Nm0xNi4yMjYuNTkyYy0uMTM3Ljc1Mi0yLjU1OCAyLjU3Ni0yLjMyMyAyLjk3Yy4wNDQuMDc0LjExLjEwNi4xODYuMTA2Yy4zMzIgMCAuODgtLjU2OC44OC0uNTY4czIuMDM0LTEuODQgMi44OTYtMS44NGMuMTEyIDAgLjIwNC4wMy4yNjkuMTAxYy41NjYuNjEzLS40NDcgMS4wODgtMS44NjUgMS45NDJjLTEuNDE5Ljg1My0xLjUxIDEuMTE2LTEuMzA5IDEuNDRxLjAxOC4wMjcuMDY0LjAyN2MuNDAyIDAgMi4zMTgtMS40OTMgMy4xNzItMS40OTNjLjE5OCAwIC4zNC4wNzkuMzkxLjI3NmMuMjk0IDEuMTEyLTMuMjEgMS4zNi0yLjk4NCAyLjE2NGMuMDMyLjExNy4xMTUuMjAzLjIyOC4yMDNjLjUwNSAwIDEuNjgyLS45NTUgMi4zMjgtLjk1NWMuMTYgMCAuMjg3LjA1OC4zNjQuMjAzYy40NTkuODY2LTMuMTYzIDEuODE1LTMuMTkyIDEuODIyYy0uNTk2LjE1NC0xLjY2LjMzNi0yLjY5Ny4zMzZjLS42MzYgMC0xLjI2MS0uMDQtMS43NjQtLjI2YTEuOSAxLjkgMCAwIDEtLjczOS0uNjI0Yy0uMDQtLjA2OS0uMTAyLS4xNDgtLjE0Mi0uMjA1Yy0uNTczLS45NjgtLjQ1NS0xLjczOC40OS0yLjY3NmMxLjAyNi0xLjAxOSAxLjYyMS0yLjUwOCAxLjYyMS0yLjUwOHMuMjA1LS43OS42NjYtLjc5YS40LjQgMCAwIDEgLjA2Ny4wMDRjLjUwOC4wOC44OCAxLjM3NC0uMTg0IDIuMTY1Yy0uNzA3LjUyNS0uMzguOTQuMDQuOTRhLjY2LjY2IDAgMCAwIC41ODEtLjM1NGMuNDEtLjc0MyAxLjUyNy0yLjY1MyAyLjEwNi0zLjAxOGMuNTU5LS4zNTMuOTktLjE4Mi44NS41OTIiLz48L3N2Zz4="
gitUrl = "my_portfolio/images/github-142-svgrepo-com.svg"
resumeLink = "https://drive.google.com/file/d/1Wrusv4JYEHxucI59XdFPHw_3LMpW_2E4/view?usp=sharing"
# colors = [Input(type="color", value=o) for o in ('#e66465', '#53d2c5', '#f6b73c')]
# show(Grid(*colors))


@rt('/')
def home():
    page = Html(
    Head(
        Meta(charset='utf-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1'),
        Meta(name='color-scheme', content='light dark'),
        Link(href='https://cdn.jsdelivr.net/npm/daisyui@3.1.0/dist/full.css', rel='stylesheet', type='text/css'),
        Link(rel='stylesheet', href='https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200'),
        Script(src='https://unpkg.com/@picojs/picojs@latest/pico.min.js'),
        
        Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css'),
        Link(href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css', rel='stylesheet'),
        # Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css'),
        Link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/owl-carousel/1.3.3/owl.carousel.min.css'),
        Link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/owl-carousel/1.3.3/owl.theme.min.css'),
        Link(rel='stylesheet', href='my_portfolio/styles/style.css'),
        Link(rel='stylesheet', href='my_portfolio/styles/style2.css'),
        Title('Sanket - AI Engineer | Portfolio'),
        Link(rel='icon', href='my_portfolio/images/dinoLogo.png'),
        Style(".material-symbols-outlined {\r\n            font-variation-settings:\r\n            'FILL' 0,\r\n            'wght' 400,\r\n            'GRAD' 0,\r\n            'opsz' 48\r\n        }\r\n        /* Custom Scrollbar */\r\n        ::-webkit-scrollbar {\r\n            width: 10px;\r\n        }\r\n\r\n        ::-webkit-scrollbar-track {\r\n            background: #f1f1f1;\r\n        }\r\n\r\n        ::-webkit-scrollbar-thumb {\r\n            background: #888;\r\n        }\r\n\r\n        ::-webkit-scrollbar-thumb:hover {\r\n            background: #555;\r\n        }\r\n\r\n        /* Webcam Styling */\r\n        #camera {\r\n            width: 320px;\r\n            height: 240px;\r\n            border: 1px solid black;\r\n        }\r\n\r\n        .invisible {\r\n            display: none;\r\n        }\r\n\r\n        /* Card Layout - No Tailwind */\r\n        .card-container {\r\n            display: flex;\r\n            flex-wrap: wrap;\r\n            justify-content: center;\r\n        }\r\n\r\n        .card {\r\n            background-color: #3e4b50;\r\n            border-radius: 8px;\r\n            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);\r\n            margin: 1rem;\r\n            overflow: hidden; /* Ensure image stays within card borders */\r\n            width: 250px; /* Adjust width as needed */\r\n            transition: transform 0.3s ease; /* Add a smooth transition */\r\n        }\r\n\r\n        .card:hover {\r\n            transform: translateY(-5px); /* Lift the card slightly on hover */\r\n        }\r\n\r\n        .card img {\r\n            width: 100%;\r\n            height: 200px; /* Adjust height as needed */\r\n            object-fit: cover; /* Ensure image covers the area nicely */\r\n        }\r\n\r\n        .card-body {\r\n            padding: 1rem;\r\n        }\r\n\r\n        .card-title {\r\n            font-size: 1.25rem;\r\n            margin-bottom: 0.5rem;\r\n        }\r\n\r\n        .card-text {\r\n            color: #eeeeee;\r\n            font-size: 0.9rem;\r\n        }"),
        Style("""
              
              .centered {
        text-align: center;
    }
    .btn-space {
    margin-right: 15px;
}
              """)
    ),
    Body(
        Main(
            Nav(
                Ul(
                    Image(src='images/dinoLogo.png',style="width:40px"),
                    Li(
                        Strong('Sanket Dhuri')
                    )
                ),
                Ul(
                    Li(
                        A('Home', href='#home')
                    ),
                    Li(
                        A('About', href='#about')
                    ),
                    Li(
                        A('Skills', href='#skills')
                    ),
                    Li(
                        A('Experience', href='#experince')
                    ),
                    Li(
                        A('Education', href='#eduction')
                    ),
                    Li(
                        A('Projects', href='#main-slider')
                    ),
                )
            ),
            Br(),
            Br(),
            Div(
                Div(
                    Br(),
                    Br(),
                    # Div(
                    #     H1("Hi, I'm Sanket", cls='home__title'),
                    #     H3('and I ❤️ AI', cls='home__subtitle'),
                    # ),
                     Div(
                            A(
                                Image(src=linkedinurl,style="width:40px"),
                                href='https://www.linkedin.com/in/sanket-dhuri-0b155815a/',
                                target='_blank',
                                cls='home__social-icon',
                                style="padding:5%"
                                
                            ),
                            A(
                                Image(src=gitUrl,style="width:40px"),
                                href='https://github.com/spdraptor',
                                target='_blank',
                                cls='home__social-icon',
                                style="padding:5%"
                            ),
                            A(
                                Image(src=hfurl,style="width:40px"),
                                href='https://huggingface.co/spdraptor',
                                target='_blank',
                                cls='home__social-icon',
                                style="padding:5%"
                            ),
                            
                            cls='home__social',
                            style="width:10%;justify-self: right;",
                        ),
                    Div(
                        H1("Hi, I'm Sanket", cls='home__title'),
                        H3('and I ❤️ AI', cls='home__subtitle'),
                        P(
                            '2+ yrs EXP | Genrative AI | Deep Learning | Machine Learning',
                            Br(),
                            Br(),
                            cls='home__description'
                        ),
                        Container(
                        Button('See Resume',onclick="window.open('https://drive.google.com/file/d/1Wrusv4JYEHxucI59XdFPHw_3LMpW_2E4/view?usp=sharing', '_blank');" ,cls='outline btn-space'),
                        # Span(),
                        Button('Contact',onclick="window.location.href = '#contact';", cls='outline btn-space'),
                        )
                    ),
                    Div(              
                            Svg(
                                Mask(
                                    Path(d='M190.312 36.4879C206.582 62.1187 201.309 102.826 182.328 134.186C163.346 165.547 \r\n                                    130.807 187.559 100.226 186.353C69.6454 185.297 41.0228 161.023 21.7403 129.362C2.45775 \r\n                                    97.8511 -7.48481 59.1033 6.67581 34.5279C20.9871 10.1032 59.7028 -0.149132 97.9666 \r\n                                    0.00163737C136.23 0.303176 174.193 10.857 190.312 36.4879Z'),
                                    id='mask0',
                                    mask_type='alpha'
                                ),
                                G(
                                    Path(d='M190.312 36.4879C206.582 62.1187 201.309 102.826 182.328 134.186C163.346 \r\n                                    165.547 130.807 187.559 100.226 186.353C69.6454 185.297 41.0228 161.023 21.7403 \r\n                                    129.362C2.45775 97.8511 -7.48481 59.1033 6.67581 34.5279C20.9871 10.1032 59.7028 \r\n                                    -0.149132 97.9666 0.00163737C136.23 0.303176 174.193 10.857 190.312 36.4879Z'),
                                    Image(x='25', y='12',width="160", height="160", **{'xlink:href':'my_portfolio/images/symbol.png'}, 
                                        cls='home__blob-img'
                                        ),
                                    mask='url(#mask0)'
                                ),
                                viewbox='0 0 200 187',
                                cls='home__blob'
                            ),
                            style="width:40%;justify-self: center; padding:1% 10% 5% 5%",
                            cls='home__img'
                        ),
                    style="display: flex; flex-direction: row;"
                ),
                cls='home__content grid',
                id='home'
            ),
            
            Br(),
            Br(),

            Section(
                    Br(),
                    Br(),
                    H2('About', cls='section__title centered'),
                    P('My Introduction', cls='section__subtitle centered'),
                    Div(
                        # Img(src='demo.jpeg', alt='add good pic here', cls='about__img'),
                        Div(
                            P('I am AI Developer/Engineer with 2+ years of expertise in Deep Learning, Model Deployment, and Gen. AI . My professional journey has been marked by diverse projects in Computer Vision and Generative Adversarial Networks (GANs). I am skilled in Python, TensorFlow, PyTorch, among other pivotal frameworks and libraries. My drive lies in devising innovative AI solutions that have a significant impact', cls='about__description'),
                            Div(
                                Div(
                                    Span(U('02+'), cls='about__info-title'),
                                    Span(U(' of Years XP'), cls='about__info-name'),
                                    style="padding:10px"
                                ),
                                Div(
                                    Span(U('03+'), cls='about__info-title'),
                                    Span(U('Projects'), cls='about__info-name'),
                                    style="padding:10px"
                                ),
                                Div(
                                    Span(U('10+'), cls='about__info-title'),
                                    Span(U('Pocs'), cls='about__info-name'),
                                    style="padding:10px"
                                ),
                                style="justify-content: center;display: flex; flex-direction: row;",
                                # style="display: flex; flex-direction: row;"
                                cls='about__info'
                            ),
                            # Div(
                            #     A(
                            #         'Leave a message',
                            #         I(cls='uil uil-comment-download button__icon'),
                            #         href='#contact',
                            #         cls='button button--flex'
                            #     ),
                            #     cls='about__buttons'
                            # ),
                            
                            cls='about__data'
                        ),
                        cls='about__container container grid'
                    
                        ),
                        id='about',
                        cls='section'
                ),
            
            Br(),
            Br(),
            
            Section(
                Br(),
                Br(),
                H2('Skills', cls='section__title centered'),
                P('My technical & miscellaneous skills', cls='section__subtitle centered'),
                Div(
                    Div(
                        Div(
                            Span('code', cls='material-symbols-outlined text-5xl'),
                            H2('Programming', cls='card-title'),
                            P('Python', cls='card-text'),
                            cls='card-body items-center flex-col'
                        ),
                        cls='card'
                    ),
                    Div(
                        Div(
                            Span('data_object', cls='material-symbols-outlined text-5xl'),
                            H2('Machine Learning', cls='card-title'),
                            P('PyTorch,Tensorflow', cls='card-text'),
                            cls='card-body items-center flex-col'
                        ),
                        cls='card'
                    ),
                    Div(
                        Div(
                            Span('psychology', cls='material-symbols-outlined text-5xl'),
                            H2('Deep Learning', cls='card-title'),
                            P('CNNs, RNNs, Transformers, GANs, Difussion', cls='card-text'),
                            cls='card-body items-center flex-col'
                        ),
                        cls='card'
                    ),
                    Div(
                        Div(
                            Span('translate', cls='material-symbols-outlined text-5xl'),
                            H2('NLP', cls='card-title'),
                            P('NLTK, BERT', cls='card-text'),
                            cls='card-body items-center flex-col'
                        ),
                        cls='card'
                    ),
                    Div(
                        Div(
                            Span('rocket', cls='material-symbols-outlined text-5xl'),
                            H2('Model Deployment', cls='card-title'),
                            P('Gradio FastAPI FastHTML CoreML TFlite', cls='card-text'),
                            cls='card-body items-center flex-col'
                        ),
                        cls='card'
                    ),
                    Div(
                        Div(
                            Span('camera_alt', cls='material-symbols-outlined text-5xl'),
                            H2('Computer Vision', cls='card-title'),
                            P('OpenCV, YOLO, ImageNet, GANs, Difussion', cls='card-text'),
                            cls='card-body items-center flex-col'
                        ),
                        cls='card'
                    ),
                    Div(
                        Div(
                            Span('cloud', cls='material-symbols-outlined text-5xl'),
                            H2('Cloud Computing', cls='card-title'),
                            P('AWS', cls='card-text'),
                            cls='card-body items-center flex-col'
                        ),
                        cls='card'
                    ),
                    
                    cls='card-container'
                ),
                id='skills',
            ),
            Br(),
            Br(),
            
            Section(
                Br(),
                Br(),
                H2('Experince', cls='section__title centered'),
                P('My working experince', cls='section__subtitle centered'),
                # Br(),
                Div(
                    Li(
                        H3('Ciklum'),
                        H4('2023 - present'),
                        P('Software Engineer - AI developer / Engineer'),
                       
                        H4('2022 - 2023'),
                        P('Software Engineer - iOS ML Devloper'),
                        style="list-style-type: none;"
                        ),
                     Br(),
                    Li(
                        H3('Gadre Infotech Pvt. Ltd.'),
                        H4('2020 - 2020'),
                        P('Intern'),
                        style="list-style-type: none;"
                        ),                 
                    # cls='centered'
                    Style="padding:1% 1% 1% 1%"
                    
                    ),
                    id='experince',
                    cls='section'
                ),
             Br(),
            Br(),
            
            Section(
                Br(),
                Br(),
                H2('Eduction', cls='section__title centered'),
                P('My educational staus', cls='section__subtitle centered'),
                Div(
                    H3('Computer Engineer'),
                    H4('2022 passout'),
                    P('Mumbai University'),
                    ),
                    id='eduction',
                    cls='section'
                ),
            Div(
                Svg(
                    Path(d='M50,1 a49,49 0 0,1 0,98 a49,49 0 0,1 0,-98'),
                    width='100%',
                    height='100%',
                    viewbox='-1 -1 102 102',
                    cls='progress-circle svg-content'
                ),
                cls='progress-wrap'
            ),
           Br(),
            Br(),
            
            Section(
                Br(),
                Br(),
                H2('Projects', cls='section__title centered'),
                P('My Project Experinece', cls='section__subtitle centered'),
                Div(
                    *cards,
                    
                    id='main-slider',
                    cls='owl-carousel'
                ),
            ),
            Br(),
            Br(),
            
            Section(
                Br(),
                Br(),
                H2('Contact', cls='section__title centered'),
                P('Get in touch with me', cls='section__subtitle centered', style="font-size: medium;padd"),
                Div(
                    Div(
                        Div(
                            I(cls='uil uil-envelope contact__icon centered'),
                            Div(
                                H3('Email', cls='contact__title centered'),
                                Span('sanketdhuri360@outlook.com', cls='contact__subtitle centered')
                            ),
                            cls='contact__information centered'
                        ),
                        Br(),
                        Div(
                            I(cls='uil uil-map-marker contact__icon centered'),
                            Div(
                                H3('Location', cls='contact__title centered'),
                                Span('Pune, India', cls='contact__subtitle centered')
                            ),
                            cls='contact__information centered'
                        )
                    ),
                    cls='contact__container container grid'
                ),
                id='contact',
                cls='contact section'
            ),
        cls='container'
        ),
        Script(src='https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js'),
        Script(type='text/javascript', src='https://code.jquery.com/jquery-1.12.0.min.js'),

        Script(type='text/javascript', src='https://cdnjs.cloudflare.com/ajax/libs/owl-carousel/1.3.3/owl.carousel.min.js'),
        Script(src='my_portfolio/js_scripts/script.js'),
        
        Script(src='my_portfolio/js_scripts/script2.js')
    ),
    lang='en'
    )
    # print(page)
    return page

serve()
