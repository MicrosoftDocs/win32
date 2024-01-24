---
description: After the queue has successfully committed, you will need to update registry information for the product you are installing.
ms.assetid: 32161538-c1bd-41a0-bb4f-a32883fe8285
title: Updating Registry Information
ms.topic: article
ms.date: 05/31/2018
---

# Updating Registry Information

After the queue has successfully committed, you will need to update registry information for the product you are installing. It is recommended that you wait until all necessary file copy operations have been successfully completed before altering registry information.

One way to update the registry is to call [**SetupInstallFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfrominfsectiona) with the SPINST\_INIFILES, SPINST\_REGISTRY, or SPINST\_INI2REG flags specified. These flags can be combined in one call to **SetupInstallFromInfSection**.

The following example uses SPINST\_ALL^SPINST\_FILES to indicate that the function should process all of the listed operations except file operations. Since only INI, registry, and file operations are listed in the **Install** section, this is a shorthand method of specifying the function should process all INI and registry operations.

The following example shows how to install registry information using the **SetupInstallFromINFSection** function.

``` syntax
Test = SetupInstallFromINFSection (
     NULL,                     //Window to own any dialog boxes
                               //created 
     MyInf,                    //INF file containing the section 
     MySection,                //the section to install
     SPINST_ALL ^ SPINST_FILES,//which installation operations 
                               //to process
     NULL,                     //the relative root key
     NULL,                     //the source root path
     0,                        //copy style
     NULL,                     //Message handler routine
     NULL,                     //Context
     NULL,                     //Device info set
     NULL                      //device info data
);
```

In the example, *OwnerWindow* is **NULL** because only file operations generate dialog boxes, and thus a parent window is not needed. "MyInf" is the INF file containing the section to process. The parameter, "MySection", specifies the section to be installed. The combined flags, SPINST\_ALL ^ SPINST\_FILES, specify which installation operations to process, in this case, all operations except file operations. The source root path is specified as "A:\\".

Since no copy operations are being processed, the *CopyFlags*, *MsgHandler*, *Context*, *DeviceInfoSet*, and *DeviceInfoData* parameters are not specified.

 

 



