---
title: NDF Diagnostics Example
description: The following example shows how to launch the NDF user interface and diagnose connectivity to the website http //www.microsoft.com.
ms.assetid: 6fe3af13-7216-4ac9-91ac-c497d25521ab
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NDF Diagnostics Example

The following example shows how to launch the NDF user interface and diagnose connectivity to the website http://www.microsoft.com.


```C++
#include "ndfapi.h"

NDFHANDLE hNDF;
HRESULT hr = NdfCreateWebIncident (
                    L"http://www.microsoft.com",
                    &amp;hNDF);

if(SUCCEEDED(hr))
{
    NdfExecuteDiagnosis(hNDF, NULL); // launches the NDF UI
                                     // the UI is not modal to the original window
    NdfCloseIncident(hNDF);
}
```



The NDF UI can be launched as a modal window. To do so, change the second parameter of [**NdfExecuteDiagnosis**](/windows/win32/Ndfapi/nf-ndfapi-ndfexecutediagnosis?branch=master) from **NULL** to the handle (HWND) of the parent window.

This example can be modified to diagnose other areas of networking. To do so, replace the [**NdfCreateWebIncident**](/windows/win32/Ndfapi/nf-ndfapi-ndfcreatewebincident?branch=master) call with one of the other incident creation functions, such as [**NdfCreateDNSIncident**](/windows/win32/Ndfapi/nf-ndfapi-ndfcreatednsincident?branch=master) or [**NdfCreateWinSockIncident**](/windows/win32/Ndfapi/nf-ndfapi-ndfcreatewinsockincident?branch=master).

## Related topics

<dl> <dt>

[**NdfCloseIncident**](/windows/win32/Ndfapi/nf-ndfapi-ndfcloseincident?branch=master)
</dt> <dt>

[**NdfCreateWebIncident**](/windows/win32/Ndfapi/nf-ndfapi-ndfcreatewebincident?branch=master)
</dt> <dt>

[**NdfExecuteDiagnosis**](/windows/win32/Ndfapi/nf-ndfapi-ndfexecutediagnosis?branch=master)
</dt> </dl>

 

 




