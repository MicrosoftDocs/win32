---
description: You can extract files from a cabinet in two ways. The first and simplest way is to take advantage of the automatic cabinet processing built into the setup functions.
ms.assetid: 113333c8-28d1-4b0e-8da4-0c94389d8038
title: Extracting Files from Cabinets
ms.topic: article
ms.date: 05/31/2018
---

# Extracting Files from Cabinets

You can extract files from a cabinet in two ways. The first and simplest way is to take advantage of the automatic cabinet processing built into the setup functions.

The installation functions, such as [**SetupCommitFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupcommitfilequeuea), [**SetupInstallFile**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfilea), and [**SetupInstallFromInfSection**](/windows/desktop/api/Setupapi/nf-setupapi-setupinstallfrominfsectiona), check the compression on each file. If the file is in a cabinet, the functions first search for a file of that name outside the cabinet. If found, the functions install the external file, ignoring the file inside the cabinet. This enables you to update a single file inside the cabinet without rebuilding the cabinet.

The setup functions also track which files in a cabinet have been retrieved, so that a file is extracted only once, even if it is installed several times.

The second way to extract files from a cabinet is by using [**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta). This function iterates through each file in a cabinet, sending a notification to a callback routine for each file found. The callback routine then returns a value that indicates whether the file should be extracted or skipped.

> [!Note]  
> The Setup API does not supply a default callback routine to handle cabinet notifications. If you call [**SetupIterateCabinet**](/windows/desktop/api/Setupapi/nf-setupapi-setupiteratecabineta) explicitly, you must supply a callback routine to process the cabinet notifications that the function returns.

 

 

 



