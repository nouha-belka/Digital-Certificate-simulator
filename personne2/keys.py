from pathlib import Path

public =  (65989367294638169625042944734247719984056321543477647178336414274681086245381581720330729774912013654745594153603930391301964551975376676386103388055049400489492354454591917285851679434557627087734551473021727258779284268999586158348791539050516506541121961505930662073110629457642398764758927450372155180781, 65537)
private =  (65989367294638169625042944734247719984056321543477647178336414274681086245381581720330729774912013654745594153603930391301964551975376676386103388055049400489492354454591917285851679434557627087734551473021727258779284268999586158348791539050516506541121961505930662073110629457642398764758927450372155180781, 32348755711656628706589479003878366417867425152620754244143216525057284553845523535240632855922582093870816536808725936209442225938216984028203053970193502405002679867879399137142165698571127039694157451159793185574917435155881415532524560683261797179478658668727788235135361699624642137206233641098887788517)

name = "houda"
lastName = "touati"
email = "houdatouati@gmail.com"

hashFunction = "\nsha256\nsign\n"

info = name + "/" + lastName + "/" + email + "\n"

fileToBeEnc = Path(__file__).with_name(f'{name}.txt')

with open(fileToBeEnc, 'w') as f:
    f.write(info)
    f.write(str(public))
    f.write(hashFunction)