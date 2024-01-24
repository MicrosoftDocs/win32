---
description: The \_ForceCodepage table is a special table used for changing the code page of an installation package. You can determine or set the code page by exporting or importing a text archive file named \_ForceCodepage.idt.
ms.assetid: d95c205f-a800-4a63-a712-6f06675e4a8a
title: '_ForceCodepage'
ms.topic: article
ms.date: 05/31/2018
---

# \_ForceCodepage

The \_ForceCodepage table is a special table used for changing the code page of an installation package. You can determine or set the code page by exporting or importing a [text archive file](text-archive-files.md) named \_ForceCodepage.idt.

The format of the \_ForceCodepage table is 2 blank lines followed by a third line that indicates the numeric code page. For example, a \_ForceCodepage table .idt file for a Japanese database would look as follows. The numeric code page in this case is 932.

``` syntax
<- this line blank
<- this line blank
932 _ForceCodepage
```

For more information on how to use \_ForceCodepage to get or set the code page of a database see the following topics.

-   [Code Page Handling (Windows Installer)](code-page-handling-windows-installer-.md)
-   [Determining an Installation Database's Code Page](determining-an-installation-database-s-code-page.md)
-   [Setting the Code Page of a Database](setting-the-code-page-of-a-database.md)

The \_ForceCodepage table is a special pseudo table used for changing the code page of an installation package. Using the \_ForceCodepage table unconditionally sets the database to the code page without performing any validation as to whether the data currently in the database can be translated to the new code page. It is always recommended that changing the code page of a database start with a language neutral database.

 

 



