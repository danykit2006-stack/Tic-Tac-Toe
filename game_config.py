import math

# Représentation de la grille : liste de 9 cases
# Index : 0 1 2
#         3 4 5
#         6 7 8

def afficher_grille(board):
    print()
    for i in range(3):
        ligne = board[3*i:3*i+3]
        print(" | ".join(c if c != " " else "." for c in ligne))
    print()

def joueur_gagnant(board, joueur):
    lignes_gagnantes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # lignes
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # colonnes
        (0, 4, 8), (2, 4, 6)              # diagonales
    ]
    for a, b, c in lignes_gagnantes:
        if board[a] == board[b] == board[c] == joueur:
            return True
    return False

def cases_libres(board):
    return [i for i, c in enumerate(board) if c == " "]

def partie_terminee(board):
    return joueur_gagnant(board, "X") or joueur_gagnant(board, "O") or len(cases_libres(board)) == 0

def evaluation(board):
    if joueur_gagnant(board, "O"):
        return 1   # IA gagne
    elif joueur_gagnant(board, "X"):
        return -1  # humain gagne
    else:
        return 0   # nul ou non terminé (dans Minimax, on gère ça)

def minimax(board, maximising):
    # maximising = True -> IA (O)
    # maximising = False -> humain (X)
    if partie_terminee(board):
        return evaluation(board)

    if maximising:
        meilleur_score = -math.inf
        for move in cases_libres(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = " "
            meilleur_score = max(meilleur_score, score)
        return meilleur_score
    else:
        meilleur_score = math.inf
        for move in cases_libres(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = " "
            meilleur_score = min(meilleur_score, score)
        return meilleur_score

def meilleur_coup_ia(board):
    meilleur_score = -math.inf
    meilleur_move = None
    for move in cases_libres(board):
        board[move] = "O"
        score = minimax(board, False)
        board[move] = " "
        if score > meilleur_score:
            meilleur_score = score
            meilleur_move = move
    return meilleur_move

def tour_humain(board):
    while True:
        try:
            choix = int(input("Ton coup (0-8) : "))
            if choix in cases_libres(board):
                board[choix] = "X"
                break
            else:
                print("Case occupée ou invalide.")
        except ValueError:
            print("Entre un nombre entre 0 et 8.")

def jeu():
    print("Bienvenue dans le jeu du Morpion !")
    board = [" "] * 9
    print("Morpion avec IA Minimax (X = toi, O = IA)")
    afficher_grille(board)

    while not partie_terminee(board):
        # Tour humain
        tour_humain(board)
        afficher_grille(board)
        if partie_terminee(board):
            break

        # Tour IA
        print("Tour de l'IA...")
        move = meilleur_coup_ia(board)
        board[move] = "O"
        afficher_grille(board)

    # Résultat
    if joueur_gagnant(board, "X"):
        print("Tu as gagné !")
    elif joueur_gagnant(board, "O"):
        print("L'IA a gagné.")
    else:
        print("Match nul.")

if __name__ == "__main__":
    jeu()
