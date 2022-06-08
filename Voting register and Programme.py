def condorcet(self):  
    count_register = self.__makecountregister__()
    roundList = []  # list of possible
    fillingList = True
    lengthofRoundList = 0.5 * (len(count_register.candidates) ** 2) - 0.5 * len(count_register.candidates)
    while fillingList:  
        r1 = random.randint(0, len(count_register.candidates) - 1)
        r2 = random.randint(0, len(count_register.candidates) - 1)
        if r1 != r2:
            if not containsBoth(roundList, r1, r2):  
                roundList.append([r1, r2])
        if len(roundList) == lengthofRoundList:
            fillingList = False

    for ro in roundList:
        c1 = 0  
        c2 = 0  
        for b in self.registry.br:
            if isHigherThan(b, ro[0], ro[1]):
                c1 += 1
            else:
                c2 += 1
        if c1 > c2:
            count_register.votes[ro[0]] += 1  
        if c2 > c1:
            count_register.votes[ro[1]] += 1  

    biggest_num = 0
    for v in range(len(count_register.votes)):  
        if count_register.votes[v] > biggest_num:
            biggest_num = count_register.votes[v]

    count = 0
    for v in range(len(count_register.votes)):  
        if count_register.votes[v] == biggest_num:
            count += 1

    if count > 1:
        print("It's a tie!")
    else:
        winner = ""
        for c in range(len(
                count_register.candidates)):  
            if count_register.votes[c] == biggest_num:
                winner = count_register.candidates[c]

        print("Winner is", winner)