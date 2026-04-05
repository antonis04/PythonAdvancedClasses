
import random


CHOICES = {
	"K": "Kamień",
	"P": "Papier",
	"N": "Nożyce",
}


def determine_winner(user_choice, computer_choice):
	if user_choice == computer_choice:
		return "draw"

	winning_pairs = {
		("K", "N"),
		("P", "K"),
		("N", "P"),
	}
	return "user" if (user_choice, computer_choice) in winning_pairs else "computer"


def get_user_choice():
	while True:
		choice = input("Wybierz K (Kamień), P (Papier) lub N (Nożyce): ").strip().upper()
		if choice in CHOICES:
			return choice
		print("Nieprawidłowy wybór. Wpisz K, P albo N.")


def play_round(user_score, computer_score, draws):
	user_choice = get_user_choice()
	computer_choice = random.choice(list(CHOICES.keys()))

	print(f"Ty: {CHOICES[user_choice]} | Komputer: {CHOICES[computer_choice]}")

	winner = determine_winner(user_choice, computer_choice)
	if winner == "user":
		user_score += 1
		print("Wygrywasz tę rundę.")
	elif winner == "computer":
		computer_score += 1
		print("Komputer wygrywa tę rundę.")
	else:
		draws += 1
		print("Remis.")

	print(f"Aktualny wynik -> Ty: {user_score}, Komputer: {computer_score}, Remisy: {draws}")
	print("-" * 40)
	return user_score, computer_score, draws


def main():
	user_score = 0
	computer_score = 0
	draws = 0

	print("Gra w Kamień, Papier i Nożyce rozpoczęta. Przerwij działanie skrótem Ctrl+C.")

	try:
		while True:
			user_score, computer_score, draws = play_round(user_score, computer_score, draws)
	except KeyboardInterrupt:
		print("\nGra przerwana przez użytkownika.")
		print(f"Końcowy wynik -> Ty: {user_score}, Komputer: {computer_score}, Remisy: {draws}")


if __name__ == "__main__":
	main()

