def main():
      idade = int (input("me diga a sua idade: "))

      if idade >=  18:
         print("você pode entrar")

      elif idade >= 16:
         acomp = input("você esta acompanhado?")

         if acomp == "sim":
               print("você pode entrar")
         else :
               print ("você não pode entar")
         
      else :
            print("entrada proibida")


      return 0
main() 