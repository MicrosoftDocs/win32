---
Description: Evalcom2.dll can be used to implement validation operations for installation packages and merge modules using Internal Consistency Evaluators - ICEs.
ms.assetid: df38e75e-554c-4a6d-b9ad-8eee5123a16f
title: Using Evalcom2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Evalcom2

Evalcom2.dll can be used to implement validation operations for installation packages and merge modules using [Internal Consistency Evaluators - ICEs](internal-consistency-evaluators-ices.md). The main object implements interfaces for C/C++ programs.

The main object also implements [Evalcom2 interfaces](evalcom2-interfaces.md) for C/C++ programs. The CLSID required to obtain the interface from [**CoCreateInstance**](_com_cocreateinstance) is {6E5E1910-8053-4660-B795-6B612E29BC58}. The REFIID is {E482E5C6-E31E-4143-A2E6-DBC3D8E4B8D3}.

You can use the following procedure to implement validation operations.

**To implement validation operations**

1.  Initialize COM on the calling thread using [**CoInitialize**](_com_coinitialize).
2.  Obtain the pointer to the [**IValidate**](/windows/win32/evalcom2/nn-evalcom2-ivalidate?branch=master) interface using [**CoCreateInstance**](_com_cocreateinstance).
3.  Open the installation package or merge module using the [**OpenDatabase**](/windows/win32/evalcom2/nf-evalcom2-ivalidate-opendatabase?branch=master) method.
4.  Open the evaluation file using the [**OpenCUB**](/windows/win32/evalcom2/nf-evalcom2-ivalidate-opencub?branch=master) method.
5.  Set the display callback function using the [**SetDisplay**](/windows/win32/evalcom2/nf-evalcom2-ivalidate-setdisplay?branch=master) method.
6.  Set the status callback function using the [**SetStatus**](/windows/win32/evalcom2/nf-evalcom2-ivalidate-setstatus?branch=master) method.
7.  Perform the validation using the [**Validate**](/windows/win32/evalcom2/nf-evalcom2-ivalidate-validate?branch=master) method.
8.  Close the .cub file using the [**CloseCUB**](/windows/win32/evalcom2/nf-evalcom2-ivalidate-closecub?branch=master) method.
9.  Close the database using the [**CloseDatabase**](/windows/win32/evalcom2/nf-evalcom2-ivalidate-closedatabase?branch=master) method.
10. Release the [**IValidate**](/windows/win32/evalcom2/nn-evalcom2-ivalidate?branch=master) interface.
11. Uninitialize COM using [**CoUninitialize**](_com_couninitialize).

## Related topics

<dl> <dt>

[Evalcom2 Interfaces](evalcom2-interfaces.md)
</dt> <dt>

[Validation Automation](validation-automation.md)
</dt> <dt>

[Validation Callback Functions](validation-callback-functions.md)
</dt> </dl>

 

 



