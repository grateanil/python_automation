def toolname(security, analysis):
    print("Tools,", security, analysis)

toolname("Fortify", "Sonar")


def name(fname, mtame = "Jenkins", boardname = "Jira"):
    print("Hello,", fname, mtame, boardname)

name("Sonar")


def name(firsttool, secondtool, thirdtool):
    print("Hello,", firsttool, secondtool, thirdtool)

name(thirdtool = "Ansible", firsttool = "Terraform", secondtool = "Jmeter")


def name(firsttool, secondtool, thirdtool):
    print("Hello,", firsttool, secondtool, thirdtool)

name("Ansible", "Terraform", "Jmeter")



def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("Ansible", "Terraform", "Jmeter")
