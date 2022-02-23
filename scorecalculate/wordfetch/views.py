from datetime import datetime
import os

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_scores(request):
    # try:
        # Method to accept the word from the user
        if request.method == "POST":
            input_word = request.POST["inputWord"]
            if input_word:
                list_of_characters = list(input_word)
                current_datetime = str(datetime.now()).split(".")[0]

                # Compute score
                final_score = 0
                score_breakdown = []
                for alphabet in list_of_characters:
                    if alphabet.lower() in ['a', 'b', 'c', 'd', 'e', 'z']:
                        final_score = final_score + 1
                        individual_breakdown = (alphabet.lower(), 1)
                        score_breakdown.append(individual_breakdown)
                    elif alphabet.lower() in ['f', 'g', 'h', 'i', 'j', 'k']:
                        final_score = final_score + 2
                        individual_breakdown = (alphabet.lower(), 2)
                        score_breakdown.append(individual_breakdown)
                    elif alphabet.lower() in ['l', 'm', 'n', 'o',]:
                        final_score = final_score + 3
                        individual_breakdown = (alphabet.lower(), 2)
                        score_breakdown.append(individual_breakdown)
                    elif alphabet.lower() in ['p', 'q', 'r', 's', 't']:
                        final_score = final_score + 4
                        individual_breakdown = (alphabet.lower(), 4)
                        score_breakdown.append(individual_breakdown)
                    elif alphabet.lower() in ['u', 'v', 'w', 'x', 'y']:
                        final_score = final_score + 5
                        individual_breakdown = (alphabet.lower(), 5)
                        score_breakdown.append(individual_breakdown)
                    else:
                        # Means it's not used in the final score
                        individual_breakdown = (alphabet, 0)
                        score_breakdown.append(individual_breakdown)
                        continue

                output_data = "{}~{}~{}\n".format(input_word, final_score, current_datetime)

                with open(os.path.join(os.getcwd(), "wordfetch/history.txt"), "a") as input_file:
                    input_file.write(output_data)
                # Return a response
                # print(score_breakdown)
                return render(request, 'wordfetch/score.html', {
                    'inputWord': input_word,
                    'outputScore': final_score,
                    'scoreBreakdown': score_breakdown,
                    'currentDatetime': current_datetime
                })
            else:
                return HttpResponse("Word is empty")
        else:
            return HttpResponse("Method not supported")

def home_page(request):
    current_datetime = str(datetime.now())
    return render(request, 'wordfetch/index.html', {
        "currentDatetime": current_datetime.split(".")[0]
    })

def display_scores(request):
    with open(os.path.join(os.getcwd(), "wordfetch/history.txt"), "r") as input_file:
        input_lines = input_file.read()

    final_history = []
    for line in input_lines.split("\n"):
        if line != "\n":
            values = line.split("~")
            final_history.append(values)

    return render(request, 'wordfetch/previousscores.html', {
        "previousList": final_history
    })
