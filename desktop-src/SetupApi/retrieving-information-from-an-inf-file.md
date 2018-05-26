---
Description: After you have a handle to an INF file, you can retrieve information from it in a variety of ways. Functions such as SetupGetInfInformation, SetupQueryInfFileInformation, and SetupQueryInfVersionInformation retrieve information about the INF file itself.
ms.assetid: e64c9576-ad62-4ebd-8d30-4e4e0da3b8c5
title: Retrieving Information From an INF File
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Retrieving Information From an INF File

After you have a handle to an INF file, you can retrieve information from it in a variety of ways. Functions such as [**SetupGetInfInformation**](/windows/win32/Setupapi/nf-setupapi-setupgetinfinformationa?branch=master), [**SetupQueryInfFileInformation**](/windows/win32/Setupapi/nf-setupapi-setupqueryinffileinformationa?branch=master), and [**SetupQueryInfVersionInformation**](/windows/win32/Setupapi/nf-setupapi-setupqueryinfversioninformationa?branch=master) retrieve information about the INF file itself.

Other functions such as [**SetupGetSourceInfo**](/windows/win32/Setupapi/nf-setupapi-setupgetsourceinfoa?branch=master) and [**SetupGetTargetPath**](/windows/win32/Setupapi/nf-setupapi-setupgettargetpatha?branch=master) acquire information about the source files and target directories.

Low-level functions like [**SetupGetLineText**](/windows/win32/Setupapi/nf-setupapi-setupgetlinetexta?branch=master) and [**SetupGetStringField**](/windows/win32/Setupapi/nf-setupapi-setupgetstringfielda?branch=master) enable you to directly access information stored in a line or field of an INF file. These functions are used internally by the higher-level functions, but are also available should you need to access INF information at the line or field level.

 

 



