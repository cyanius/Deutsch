import os
import random
 
def index_check(str, file):
    map = {
        "v":1, "n":2, "adj":3, "adv":4, "other":5
    }
    i = map.get(str, 0)
    if i == 0:
        return False; 
    elif i == 1 :
        verb.writing(file)
    elif i == 2 :
        noun.writing(file)
    elif i == 3 :
        adj.writing(file)
    elif i == 4 :
        adv.writing(file)
    elif i == 5 :
        other.writing(file)
    return True
        
def check_correctness(arg_1, *arg_2):
    
    print(arg_1)
    for arg in arg_2:
        print(arg);
    
    print("Is the following data correct? (Y/n)")
    if(input() != "" ):
        return  False
    else:
        return  True
        
def writing_file(file, arg_1, *arg_2):
    file.write(arg_1 + '\n')
    for arg in arg_2:
        if type(arg) != list:
            file.write(arg)
        else:
            for i in arg:
                file.write(i + '\t');
        file.write('\n')    
        

def Writing_work(char):

    with open("./" + char + ".Word", 'a' , encoding='UTF-8') as file:

        clear_level = False;
        while (not clear_level):
            part_of_speech = input("Input the part of speech of the word:");
            part_of_speech.lower();
            if not index_check(part_of_speech, file) :
                print("error, please input \"v\",\"n\", \"adj\", \"adv\" or \"other\". ");
            else:
                clear_level = True;
    

        clear_level_3 = False
        while(not clear_level_3):
            num_ex = input("Input the num of example:")
            if not (num_ex.isdigit() & (len(num_ex) == 1)):
                print("please input a number < 10.")
                continue
            
            num = int(num_ex)
            for i in range(0, num):
                m_ex = input("Input the meaning of example sentence:\n")
                ex = input("Input the example sentence:\n")
                if check_correctness(m_ex, ex):
                    clear_level_3 = True
                    writing_file(file, m_ex, ex)

class _word_:
    word_meaning = ""
    example_meaning = []
    example = []
    
    def __init__(self, word_meaning, example_meaning, example):
        self.word_meaning = word_meaning
        self.example_meaning = example_meaning
        self.example = example
        
    def read_word_meaning(self):
        return self.word_meaning
    
    def read_example_meaning(self):
        return self.example_meaning
        
    def read_example(self):
        return self.example
        
class noun(_word_):
    word_genus = ""
    word_single = ""
    word_plural = ""
    
    def __init__(self, word_meaning, word_genus, word_single, word_plural, example_meaning, example):
        super().__init__(word_meaning, example_meaning, example)
        self.word_genus = word_genus
        self.word_single = word_single
        self.word_plural = word_plural
        
    def read_word(self):
        return [self.word_genus, self.word_single, self.word_plural]
        
    @staticmethod
    def noun_writing(file):
        clear_level_2 = False
        while(not clear_level_2):
            meaning = input("N: Input the meaning of the word:")
            form = [input("N: Input the single form of the noun:"), input("N: Input the plural form of the noun:")]
            if check_correctness(meaning, form):
                clear_level_2 = True
                print("noun")
                writing_file(file, "//noun", meaning, form)
    
class verb(_word_):
    word_0_form = ""
    word_1_form = ""
    word_2_form = ""
    word_3_form = ""
    word_p_form = ""
    
    def __init__(self, word_meaning, word_0_form, word_1_form, word_2_form, word_3_form, word_p_form, example_meaning, example):
        super().__init__(word_meaning, example_meaning, example)
        self.word_0_form = word_0_form
        self.word_1_form = word_1_form
        self.word_2_form = word_2_form   
        self.word_3_form = word_3_form
        self.word_p_form = word_p_form
    
    def read_word(self):
        return [self.word_0_form, self.word_1_form, self.word_2_form, self.word_3_form, self.word_p_form]
    
    @staticmethod
    def writing(file):
        clear_level_2 = False
        while(not clear_level_2):
            meaning = input("V: Input the meaning of the word:")
            conjugation = [input("V: Input the origin form of the verb:"), input("V: Input the 1st-person form of the verb:"),\
            input("V: Input the 2nd-person form of the verb:"), input("V: Input the 3rd-person form of the verb:"),\
            input("V: Input the perfekt form of the verb:")]
            if check_correctness(meaning, conjugation):
                clear_level_2 = True
                writing_file(file, "//verb", meaning, conjugation )

class adj(_word_):
    word = ""
    
    def __init__(self, word_meaning, word, example_meaning, example):
        super().__init__(word_meaning, example_meaning, example)
        self.word = word
        
    def read_word(self):
        return self.word
        
    @staticmethod
    def writing(file):
        clear_level_2 = False
        while(not clear_level_2):
            meaning = input("Adj: Input the meaning of the word:")
            form =  input("Adj: Input the adj:")
            if check_correctness(meaning, form):
                clear_level_2 = True
                writing_file(file, "//adj", meaning, form)
        
class adv(_word_):
    word = ""

    def __init__(self, word_meaning, word, example_meaning, example):
        super().__init__(word_meaning, example_meaning, example)
        self.word = word
        
    def read_word(self):
        return self.word
    
    @staticmethod
    def writing(file):
        clear_level_2 = False
        while(not clear_level_2):
            meaning = input("Adv: Input the meaning of the word:")
            form =  input("Adv: Input the adv:")
            if check_correctness(meaning, form):
                clear_level_2 = True
                writing_file(file, "//adv", meaning, form)

class other(_word_):
    word = ""

    def __init__(self, word_meaning, word, example_meaning, example):
        super().__init__(word_meaning, example_meaning, example)
        self.word = word
        
    def read_word(self):
        return self.word
        
    @staticmethod
    def writing(file):
        clear_level_2 = False
        while(not clear_level_2):
            meaning = input("Other: Input the meaning of the word:")
            form =  input("Other: Input the word:")
            if check_correctness(meaning, form):
                clear_level_2 = True
                writing_file(file, "//other", meaning, form)
    
def Reading_work(char, word_list):

    word_count = 0
    with open("./" + char + ".Word", 'r' , encoding='UTF-8') as file:
        
        word_list[char] = []
        content = file.readlines()
        content = [x.strip() for x in content] 
        
        for i in range(0, len(content)):
            
            print(content[i])
            data = content[i].split()
            if(data[0].find('/',0,2) != -1):
                word_count += 1
                data[0] = data[0].strip('/')
                if (i + 5) > len(content):
                    print("Reading ./" + char + ".Word on line " + i + " Error! Check the file format.")
                    break
                if(data[0] == "noun"):
                    i += 1
                    word_meaning = content[i]
                    i += 1
                    data = content[i].split()
                    print(data)
                    word_genus = ""
                    word_single = ""
                    word_plural = ""
                    if(len(data) == 1):
                        word_single = data[0]
                    elif(len(data) == 2):
                        word_genus = data[0]
                        word_single = data[1]
                    elif(len(data) >= 3):
                        word_genus = data[0]
                        word_single = data[1]
                        word_plural = data[2]
                    i += 1
                    
                    example_meaning = []
                    example = []
                    while((i+1 < len(content)) ):
                        if(content[i].find('/',0,2) != -1):
                            break
                        example_meaning.append(content[i])
                        example.append(content[i + 1])
                        i += 2
                        
                    word_list[char].append(noun(word_meaning, word_genus, word_single,\
                    word_plural, example_meaning, example))
                    
                elif(data[0] == "verb"):
                    i += 1
                    word_meaning = content[i]
                    i += 1
                    data = content[i].split()
                    if(len(data) < 5 ):
                        print("please record 5 form of verb!")
                    word_0_form = data[0]
                    word_1_form = data[1]
                    word_2_form = data[2]
                    word_3_form = data[3]
                    word_p_form = data[4]
                    i += 1
                    
                    example_meaning = []
                    example = []
                    while((i+1 < len(content)) ):
                        if(content[i].find('/',0,2) != -1):
                            break
                        example_meaning.append(content[i])
                        example.append(content[i + 1])
                        i += 2
                    
                    word_list[char].append(verb(word_meaning, word_0_form, word_1_form,\
                    word_2_form, word_3_form, word_p_form, example_meaning, example))
                        
                else:
                    i += 1
                    word_meaning = content[i]
                    i += 1
                    word = content[i]
                    i += 1
                    
                    example_meaning = []
                    example = []
                    while((i+1 < len(content)) ):
                        if(content[i].find('/',0,2) != -1):
                            break
                        example_meaning.append(content[i])
                        example.append(content[i + 1])
                        i += 2 
                    
                    if(data[0] == "adj"):
                        word_list[char].append(adj(word_meaning, word, example_meaning, example))
                    elif(data[0] == "adv"):
                        word_list[char].append(adv(word_meaning, word, example_meaning, example))
                    elif(data[0] == "other"):
                        word_list[char].append(other(word_meaning, word, example_meaning, example))    
    
    return word_count
            
def Decoding_word(origin_str, str = ""):
    rnds = [random.randint(0, len(origin_str)-1) for _ in range(0, int(format(len(origin_str)*0.25,'.0f')))]
    #print(rnds)
    new_str = []
    
    for i in range(0, len(origin_str)):
        if(origin_str[i] == " "):
            new_str.append(" ")
            continue
        if(str == ""):
            new_str.append("_")
        else:
            new_str.append(str[i])
    
    for j in rnds:
        new_str[j] = origin_str[j]
    
    string_ = ""
    for k in new_str:
        string_ += k
    
    return string_
    
def example_sentence_test(word):
    j = 0
    for i in word.read_example_meaning():
        answer = input("Input the word example of \"" + i + "\".\n")
        
        True_word = word.read_example()[j]
        word_Hint = ""
        clear_level_2 = False
        while not clear_level_2:
            if answer == (word.read_example()[j]):
                print("Well done~\n")
                clear_level_2 = True
            elif answer == "H":
                print("next time will be better.\n")
                print(word.read_example()[j])
                clear_level_2 = True
            else:
                word_Hint = Decoding_word(True_word, word_Hint)
                answer = input( "Incorrect. Try again.\nHint: {0} \n".format(word_Hint)  )
        j += 1

def checking_answer(word):

    answer = input("Input the word means \"" + word.read_word_meaning() + "\".\n")
    if type(word) == noun:
        clear_level_1 = False
        while not clear_level_1:
            if answer == (word.read_word()[0] + " " + word.read_word()[1] + " " + word.read_word()[2]):
                print("Well done~\n")
                clear_level_1 = True
            elif answer == "H":
                print("next time will be better.\n")
                print(word.read_word()[0] + " " + word.read_word()[1] + " " + word.read_word()[2])
                clear_level_1 = True
            else:
                answer = input("If the word are noun, input genus single plural form and separated them by a space.\n")
                
        example_sentence_test(word)
    
    elif type(word) == verb:
        clear_level_1 = False
        while not clear_level_1:
            if answer == (word.read_word()[0] + " " + word.read_word()[1] + " " + word.read_word()[2] \
            + " " + word.read_word()[3] + " " + word.read_word()[4]):
                print("Well done~\n")
                clear_level_1 = True
            elif answer == "H":
                print("next time will be better.\n")
                print(word.read_word()[0] + " " + word.read_word()[1] + " " + word.read_word()[2] \
            + " " + word.read_word()[3] + " " + word.read_word()[4])
                clear_level_1 = True
            else:
                answer = input("If the word are verb, input origin, 1st, 2nd, 3rd single person and perfekt form and separated them by a space.\n")
                
        example_sentence_test(word)
            
    else:
        clear_level_1 = False
        while not clear_level_1:
            if answer == word.read_word():
                print("Well done~\n")
                clear_level_1 = True
            elif answer == "H":
                print("next time will be better.\n")
                print(word.read_word())
                clear_level_1 = True
            else:
                answer = input("Incorrect! try again.\n")
                
        example_sentence_test(word)
        
def Testing_work(word_num, word_list):

    while True:
        testing_time = input("How many times do you want to test?")
        spec_char = input("Specify the characters to test. Enter if no specified character.")
        
        
        if(testing_time.isdigit()):
            if(int(testing_time) == 0):
                break
                
            for i in range(0, int(testing_time)):
                while True:
                    if spec_char == "":
                        rand_num = random.randint(0, (word_num -1) )
                        for character in "abcdefghijklmnopqrstuvwxyz":
                            
                            if(word_list.get(character, '') == ''):
                                continue
                            
                            rand_num = rand_num - len(word_list[character])
                            if(rand_num < 0):
                                char = character
                                break
                                
                                
                    else:
                        char = random.choice(spec_char)
                    
                    if(word_list.get(char, '') != ''):
                        index = random.randint(0,len(word_list[char])-1)
                        
                        checking_answer(word_list[char][index])
                        break
                    #if we can't find the char file, continue until we found that.
                    else:
                        check_validity = False
                        for j in spec_char:
                            if(word_list.get(j, '') != ''):
                                check_validity = True
                                break
                            
                        if not check_validity:
                            print("Error input! no such character file!")
                            break
                
                #print(i)
                
        else:
            print("Input a number.\n")
            continue
        
    print("Testing Finish!")            
                
def work_check(str):
    map = {
        "w":1, "t":2, "q":3, "e":4
    }
    i = map.get(str, 0)
    if i == 0:
        return False; 
    else:
        return True

word_list = {"":[]}
read_clear = False
word_num = 0
while(True):
    work_clear = False
    
    while(not work_clear):
        work = input("Input the work to do.\n")
        if not work_check(work):
            print("error, please input \"w\", \"t\" or \"q\". Or \"e\" to exit.")
        else:
            work_clear = True

    if work == 'w':
        work_clear_2 = False
        character = ''
    
        while(not work_clear_2):
            character = input("Which character do you want to write?")
            if character.isalpha() & (len(character) == 1):
                work_clear_2 = True
            else:
                print("error , please input one alphabet")
        
        Writing_work(character)
        
    elif work == 't':
        
        character = ''
        
        
        while(not read_clear):
            for character in "abcdefghijklmnopqrstuvwxyz":
                
                if character == "z":
                    read_clear = True
        
                if not os.path.isfile("./" + character + ".Word"):
                    print("no " + character + ".Word file!")
                    continue
                word_num += Reading_work(character, word_list)
                
                
        print("Total word: ")
        print(word_num)
        Testing_work(word_num, word_list)
        
    elif work == 'q':
        print("not done")
    elif work == 'e':
        break
    
    

    

