from random_word import RandomWords
from string import ascii_lowercase

def get_num_attempts():
    # O jogador define quantas tentativas para acertar a palavra
    while True:
        num_attempts = input('Em quantas tentativas você consegue acertar a palavra? [1 - 10]')
        try:
            num_attempts = int(num_attempts)
            if 0 < num_attempts < 11:
                return num_attempts
        except ValueError:
            print('{0} não é um inteiro entre 1 e 10'.format(num_attempts))


def get_letters_in_word(word):
    # Cria a lista com todas as letras da palavra
    word_letters = []
    for letter in word:
        if letter in ascii_lowercase and letter not in word_letters:
            word_letters.append(letter)
    return sorted(word_letters)

def display_word(word, used_letters):
    for letter in word:
        if letter in used_letters or letter not in ascii_lowercase:
            print(letter + ' ', end = '')
        else:
            print('_ ', end = '')
    print('\n')

def get_next_letter(used_letters, word_letters, right_letters):
    # O jogador escolhe a próxima letra
    while True:
        next_letter = input('Chute uma letra: ').lower()
        if len(next_letter) != 1 or next_letter not in ascii_lowercase:
            print('{0} não é uma letra'.format(next_letter))
        elif next_letter in used_letters:
            print('{0} já foi chutada'.format(next_letter))
        else:
            used_letters.append(next_letter)
            if next_letter in word_letters:
                right_letters.append(next_letter)
            return next_letter

def play():
    # Fluxo do jogo
    print('Começando o jogo!\n')

    attempts_remaining = get_num_attempts()

    print('Selecionando palavra\n')
    r = RandomWords()
    word = r.get_random_word(minLength = 5)

    # Inicializa variáveis do jogo
    used_letters = []
    wrong_letters = []
    right_letters = []
    word_letters = get_letters_in_word(word)
    word_solved = False

    # loop principal do jogo
    while attempts_remaining > 0 and not word_solved:
        display_word(word, used_letters)
        print('Tentativas restantes: ', attempts_remaining)
        print('Letras utilizadas: ', wrong_letters)

        next_letter = get_next_letter(used_letters, word_letters, right_letters)
        if next_letter in word_letters:
            print('Acertou!')
        else:
            print('Esta letra não existe na palavra')
            wrong_letters.append(next_letter)
            attempts_remaining = attempts_remaining - 1

        if sorted(right_letters) == word_letters:
            word_solved = True

    # Fim do Jogo!
    print('A palavra é: ', word)
    if word_solved:
        print('Parabéns!!')
    else:
        print('Que pena, você errou...')

    try_again = input('Que continuar jogando? [s/n]')
    return try_again.lower() == 's'

if __name__ == '__main__':
    while play():
        print()