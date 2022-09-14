---
title: Creating a Variable Binding List
description: The SnmpCreateVbl function creates a new variable binding list.
ms.assetid: 18e8a04d-612f-4d85-9cff-8c541a4cdf71
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Variable Binding List

The [**SnmpCreateVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatevbl) function creates a new variable binding list. If the WinSNMP application specifies a variable name and a value, the function creates the list and adds the name and value as the first entry in the list. If the application specifies **NULL** for the variable name, the function creates an empty list.

To copy a variable binding list, call the [**SnmpDuplicateVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatevbl) function. The function creates a new variable binding list and initializes the new list with a copy of the data in the source variable binding list.

The [**SnmpCreateVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatevbl) function and the [**SnmpDuplicateVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatevbl) function allocate any necessary memory for the new variable binding list. The WinSNMP application must release the resources associated with these lists. It is recommended that the application do this by matching each call to [**SnmpCreateVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpcreatevbl) and [**SnmpDuplicateVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpduplicatevbl) with a corresponding call to the [**SnmpFreeVbl**](/windows/desktop/api/Winsnmp/nf-winsnmp-snmpfreevbl) function when it is appropriate to free the allocated memory.

 

 




