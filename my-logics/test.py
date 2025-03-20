# class Shop:
#     def xyz():
#         print("Red\nBlue\nGreen")
#         colour = input("Select any one colour:- ")
#         if colour == "Red" or colour == "red":
#             print("Dark Red=100\nLite Red=200\nRed=300")
#             colourChoice1 = input("Select 1st colour:- ")
#             colourChoice2 = input("Select 2nd colour:- ")
#             if colourChoice1 == "Dark Red" and colourChoice2 == "Dark Red":
#                 return 100 + 100
#             elif colourChoice1 == "Dark Red" and colourChoice2 == "lite Red":
#                 return 100 + 200
#             elif colourChoice1 == "Dark Red" and colourChoice2 == "Red":
#                 return 100 + 300
#             elif colourChoice1 == "Lite Red" and colourChoice2 == "Lite Red":
#                 return 200 + 200
#             elif colourChoice1 == "Lite Red" and colourChoice2 == "Dark Red":
#                 return 200 + 100
#             elif colourChoice1 == "Lite Red" and colourChoice2 == "Red":
#                 return 200 + 300
#             elif colourChoice1 == "Red" and colourChoice2 == "Red":
#                 return 300 + 300
#             elif colourChoice1 == "Red" and colourChoice2 == "Lite Red":
#                 return 300 + 200
#             elif colourChoice1 == "Red" and colourChoice2 == "Dark Red":
#                 return 300 + 100
#             else:
#                 return "Invalid colour choice"
#         elif colour == "Blue":
#             pass
#         elif colour == "green":
#             pass
#         else:
#             return "Invalid selection"


def xyz():
    print("Red\nBlue\nGreen")
    colour = input("Select any one colour:- ")
    if colour == "Red" or colour == "red":
        print("Dark Red=100\nLite Red=200\nRed=300")
        colourChoice1 = input("Select 1st colour:- ")
        colourChoice2 = input("Select 2nd colour:- ")
        if colourChoice1 == "Dark Red" and colourChoice2 == "Dark Red":
            return 100 + 100
        elif colourChoice1 == "Dark Red" and colourChoice2 == "lite Red":
            return 100 + 200
        elif colourChoice1 == "Dark Red" and colourChoice2 == "Red":
            return 100 + 300
        elif colourChoice1 == "Lite Red" and colourChoice2 == "Lite Red":
            return 200 + 200
        elif colourChoice1 == "Lite Red" and colourChoice2 == "Dark Red":
            return 200 + 100
        elif colourChoice1 == "Lite Red" and colourChoice2 == "Red":
            return 200 + 300
        elif colourChoice1 == "Red" and colourChoice2 == "Red":
            return 300 + 300
        elif colourChoice1 == "Red" and colourChoice2 == "Lite Red":
            return 300 + 200
        elif colourChoice1 == "Red" and colourChoice2 == "Dark Red":
            return 300 + 100
        else:
            return "Invalid colour choice"
    elif colour == "Blue":
        pass
    elif colour == "green":
        pass
    else:
        return "Invalid selection"
