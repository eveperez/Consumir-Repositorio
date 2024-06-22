import requests

if __name__ == '__main__':
    url = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/afc70f44-a83b-4ec8-adc3-a2fe3289fa82/d6lu3su-4f7ed4c0-3349-45cc-9cf9-df849ee5381a.jpg/v1/fill/w_1024,h_1536,q_75,strp/captus_flower_by_foxpjw_d6lu3su-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTUzNiIsInBhdGgiOiJcL2ZcL2FmYzcwZjQ0LWE4M2ItNGVjOC1hZGMzLWEyZmUzMjg5ZmE4MlwvZDZsdTNzdS00ZjdlZDRjMC0zMzQ5LTQ1Y2MtOWNmOS1kZjg0OWVlNTM4MWEuanBnIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.hXbDitqs8KBk0Yjfwpzwyd6X3sfX-wb_5RLKjUW90K0'

    # Realiza la peticion sin cargar el contenido
    response = requests.get(url, stream=True)

    #Descargar imagen
    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content(): # Descarga el contenido poco a poco
            file.write(chunk)

    response.close() # Cerrar conexion