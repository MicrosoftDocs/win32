---
description: After you have a handle to an INF file, you can retrieve information from it in a variety of ways. Functions such as SetupGetInfInformation, SetupQueryInfFileInformation, and SetupQueryInfVersionInformation retrieve information about the INF file itself.
ms.assetid: e64c9576-ad62-4ebd-8d30-4e4e0da3b8c5
title: Retrieving Information From an INF File
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Information From an INF File

After you have a handle to an INF file, you can retrieve information from it in a variety of ways. Functions such as [**SetupGetInfInformation**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetinfinformationa), [**SetupQueryInfFileInformation**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueryinffileinformationa), and [**SetupQueryInfVersionInformation**](/windows/desktop/api/Setupapi/nf-setupapi-setupqueryinfversioninformationa) retrieve information about the INF file itself.

Other functions such as [**SetupGetSourceInfo**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetsourceinfoa) and [**SetupGetTargetPath**](/windows/desktop/api/Setupapi/nf-setupapi-setupgettargetpatha) acquire information about the source files and target directories.

Low-level functions like [**SetupGetLineText**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetlinetexta) and [**SetupGetStringField**](/windows/desktop/api/Setupapi/nf-setupapi-setupgetstringfielda) enable you to directly access information stored in a line or field of an INF file. These functions are used internally by the higher-level functions, but are also available should you need to access INF information at the line or field level.

 

 



