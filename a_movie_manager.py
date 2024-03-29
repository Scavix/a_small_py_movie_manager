import PySimpleGUI as sg
import os
import json
import requests

class Movie:
    def __init__(self, title):
        self.title = title
        self.year = ''
        self.genre = ''

    def __str__(self):
        return f'{self.title} ({self.year}) - {self.genre}' if self.year and self.genre else self.title

    def pretty_print(self):
        return f'Title: {self.title}\nYear: {self.year}\nGenre: {self.genre}'


bar_menu = [
    ['File', ['New Archive', 'Open Archive', 'Save', 'Exit and Save', 'Exit']],
    ['Tools', ['Scan and Append', 'Generate Source', 'Generate Build Script']],
    ['Help', 'About...']
]

layout = [
    [sg.Menu(bar_menu)],
    [sg.Text('Movie Archive')],
    [sg.Listbox(values=[], size=(24, 10), key='-MOVIE LIST-')],
    [sg.Button('Add'), sg.Button('Edit'), sg.Button('Delete'), sg.Button('View')]
]

window = sg.Window('Movie Archive', layout, element_justification='c')
movies = []

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    if event == 'Add':
        movie_title = sg.popup_get_text('Enter movie title:')
        if movie_title:
            movies.append(Movie(movie_title))
            window['-MOVIE LIST-'].update(values=[str(movie)
                                          for movie in movies])

    elif event == 'Edit':
        selected_movie_index = window['-MOVIE LIST-'].get_indexes()[0]
        edited_movie_title = sg.popup_get_text(
            'Edit movie title:', default_text=movies[selected_movie_index].title)
        edited_movie_year = sg.popup_get_text(
            'Edit movie year:', default_text=movies[selected_movie_index].year)
        edited_movie_genre = sg.popup_get_text(
            'Edit movie genre:', default_text=movies[selected_movie_index].genre)
        if edited_movie_title or edited_movie_year or edited_movie_genre:
            movies[selected_movie_index].title = edited_movie_title
            movies[selected_movie_index].year = edited_movie_year
            movies[selected_movie_index].genre = edited_movie_genre
            window['-MOVIE LIST-'].update(values=[str(movie)
                                          for movie in movies])

    elif event == 'Delete':
        selected_movie_index = window['-MOVIE LIST-'].get_indexes()[0]
        movies.pop(selected_movie_index)
        window['-MOVIE LIST-'].update(values=[str(movie) for movie in movies])

    elif event == 'View':
        selected_movie_index = window['-MOVIE LIST-'].get_indexes()[0]
        sg.popup(movies[selected_movie_index].pretty_print())

    elif event == 'New Archive':
        movies.clear()
        window['-MOVIE LIST-'].update(values=[])

    elif event == 'Open Archive':
        filename = sg.popup_get_file('Select a movie archive to open:', no_window=True)
        if filename:
            if filename.endswith('.txt'):
                with open(filename, 'r') as file:
                    movies = [Movie(line.strip()) for line in file]
            if filename.endswith('.json'):
                with open(filename, 'r') as file:
                    movies = [Movie(**movie) for movie in json.load(file)]
            if filename.endswith('.xml'):
                with open(filename, 'r') as file:
                    movies = [Movie(**movie) for movie in json.load(file)]
            if filename.endswith('.csv'):
                with open(filename, 'r') as file:
                    movies = [Movie(line.strip()) for line in file]
            if filename.endswith('.db'):
                with open(filename, 'r') as file:
                    movies = [Movie(line.strip()) for line in file]
            if filename.endswith('.xlsx'):
                with open(filename, 'r') as file:
                    movies = [Movie(line.strip()) for line in file]
            if filename.endswith('.dat'):
                with open(filename, 'r') as file:
                    movies = [Movie(line.strip()) for line in file]
            window['-MOVIE LIST-'].update(values=[str(movie) for movie in movies])

    elif event == 'Save':
        filename = sg.popup_get_file('Save archive as:', save_as=True, no_window=True)
        if filename:
            if filename.endswith('.txt'):
                with open(filename, 'w') as file:
                    file.write('\n'.join([str(movie) for movie in movies]))
            if filename.endswith('.json'):
                with open(filename, 'w') as file:
                    json.dump([movie.__dict__ for movie in movies], file)
            if filename.endswith('.xml'):
                with open(filename, 'w') as file:
                    json.dump([movie.__dict__ for movie in movies], file)
            if filename.endswith('.csv'):
                with open(filename, 'w') as file:
                    file.write('\n'.join([str(movie) for movie in movies]))
            if filename.endswith('.db'):
                with open(filename, 'w') as file:
                    file.write('\n'.join([str(movie) for movie in movies]))
            if filename.endswith('.xlsx'):
                with open(filename, 'w') as file:
                    file.write('\n'.join([str(movie) for movie in movies]))
            if filename.endswith('.dat'):
                with open(filename, 'w') as file:
                    file.write('\n'.join([str(movie) for movie in movies]))

    elif event == 'Exit and Save':
        filename = sg.popup_get_file('Save archive as:', save_as=True, no_window=True)
        if filename:
            if filename.endswith('.txt'):
                with open(filename, 'w') as file:
                    file.write('\n'.join([str(movie) for movie in movies]))
            if filename.endswith('.json'):
                with open(filename, 'w') as file:
                    json.dump([movie.__dict__ for movie in movies], file)
            if filename.endswith('.xml'):
                with open(filename, 'w') as file:
                    json.dump([movie.__dict__ for movie in movies], file)
            if filename.endswith('.csv'):
                with open(filename, 'w') as file:
                    file.write('\n'.join([str(movie) for movie in movies]))
            if filename.endswith('.db'):
                with open(filename, 'w') as file:
                    file.write('\n'.join([str(movie) for movie in movies]))
            if filename.endswith('.xlsx'):
                with open(filename, 'w') as file:
                    file.write('\n'.join([str(movie) for movie in movies]))
            if filename.endswith('.dat'):
                with open(filename, 'w') as file:
                    file.write('\n'.join([str(movie) for movie in movies]))
        break

    elif event == 'About...':
        sg.popup('Movie Archive\nVersion 1.0\nDeveloped by: Scavix')

    elif event == 'Scan and Append':
        folder = sg.popup_get_folder('Select a folder to scan for movies:')
        if folder:
            files = os.listdir(folder)
            for file in files:
                movies.append(Movie(file))
            window['-MOVIE LIST-'].update(values=[str(movie) for movie in movies])

    elif event == 'Generate Source':
        response = requests.get("https://raw.githubusercontent.com/Scavix/a_small_py_movie_manager/main/a_movie_manager.py")
        if response.status_code == 200:
            f = open("a_movie_manager.py", "w")
            f.write(response.text)
            f.close()
            sg.popup("Done")
        else:
            sg.popup("Web site does not exist or is not reachable")

    elif event == 'Generate Build Script':
        response = requests.get("https://raw.githubusercontent.com/Scavix/a_small_py_movie_manager/main/a_movie_manager_build_script.bat")
        if response.status_code == 200:
            f = open("a_movie_manager_build_script.bat", "w")
            f.write(response.text)
            f.close()
            sg.popup("Done")
        else:
            sg.popup("Web site does not exist or is not reachable")

    else:
        break
    
window.close()
