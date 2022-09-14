---
title: Adding, Deleting, and Replacing Resources
description: This topic discusses how to add, delete, or replace resources.
ms.assetid: 15b1086e-e3a2-460a-828b-17db5105309f
ms.topic: article
ms.date: 05/31/2018
---

# Adding, Deleting, and Replacing Resources

Applications must frequently add, delete, or replace resources in executable files. Two methods can be used to accomplish these tasks. The first is to edit the resource-definition file, recompile the resources, and add the recompiled resources to the application's executable file. The second method is to copy the resource data directly into the application's executable file.

For example, to localize an English-language application for use in Norway, it may be necessary to replace the English dialog box with one using Norwegian. A developer creates an appropriate dialog box by using a dialog box editor or by writing a template in the resource-definition file. The developer then recompiles the resources and adds the new resources to the application's executable file.

If an appropriate dialog box exists in binary form, however, the developer can copy the data directly to the executable file being localized by using the following functions. The [**BeginUpdateResource**](/windows/desktop/api/Winbase/nf-winbase-beginupdateresourcea) function creates an update handle to the executable file whose resources are to be changed. The [**UpdateResource**](/windows/desktop/api/Winbase/nf-winbase-updateresourcea) function uses this handle to add, delete, or replace a resource in the executable file. The [**EndUpdateResource**](/windows/desktop/api/Winbase/nf-winbase-endupdateresourcea) function closes the handle.

After an update handle to an executable file is created by [**BeginUpdateResource**](/windows/desktop/api/Winbase/nf-winbase-beginupdateresourcea), an application can use [**UpdateResource**](/windows/desktop/api/Winbase/nf-winbase-updateresourcea) repeatedly to make changes to the resource data. Each call to **UpdateResource** contributes to an internal list of additions, deletions, and replacements but does not actually write the data to the executable file. Immediately before closing the update handle, [**EndUpdateResource**](/windows/desktop/api/Winbase/nf-winbase-endupdateresourcea) writes the accumulated changes to the executable file.

Sometimes, an application must copy resources from another file. [Updating Resources](using-resources.md) shows an example of obtaining the resource data and its size from a file.

 

 




