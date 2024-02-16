ToolsData = ["Maven", "Ansible", "Jenkins", "Sonar"] 
if "Maven" in ToolsData:
    print("Maven is present.")
else:
    print("Maven is absent.")


ToolsData.append("Fortify")

print(ToolsData)

del ToolsData[3]

print(ToolsData)
