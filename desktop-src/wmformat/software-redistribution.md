---
title: Software Redistribution
description: Software Redistribution
ms.assetid: 443df640-e74c-4903-b801-f4bd42a04659
keywords:
- Windows Media Format SDK,software redistribution
- Advanced Systems Format (ASF),software redistribution
- ASF (Advanced Systems Format),software redistribution
- Windows Media Format SDK,redistribution
- Advanced Systems Format (ASF),redistribution
- ASF (Advanced Systems Format),redistribution
- software redistribution,about
- redistribution,about
ms.topic: article
ms.date: 05/31/2018
---

# Software Redistribution

The inclusion of Windows Media Format software in an application setup is known as redistribution. The Windows Media Format SDK includes an installation package which can be included with your application setup. The installation package is an executable file named wmfdist95.exe. When you install the Windows Media Format SDK, the installation package is copied to the \\Redist folder of the install directory (c:\\wmsdk\\wmfsdk by default).

The following sections provide procedures and other information for software redistribution setup.



| Section                                                                            | Description                                                                                                                                                                      |
|------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [To Create a Redistribution Setup](to-create-a-redistribution-setup.md)           | Describes the procedure for creating an application setup.                                                                                                                       |
| [Detecting Setup Status](detecting-setup-status.md)                               | Provides example code that checks the registry for installation status to determine whether the redistribution package needs to be installed.                                    |
| [Example Code for Redistribution Setup](example-code-for-redistribution-setup.md) | Provides example code that can be used in your setup routine to run the redistribution packages in quiet mode and notify your setup routine when the computer must be restarted. |



 

## Related topics

<dl> <dt>

[**Project Considerations**](project-considerations.md)
</dt> </dl>

 

 




