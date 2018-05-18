---
title: NDF Diagnostics Example
description: The following example shows how to launch the NDF user interface and diagnose connectivity to the website http //www.microsoft.com.
ms.assetid: '6fe3af13-7216-4ac9-91ac-c497d25521ab'
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



The NDF UI can be launched as a modal window. To do so, change the second parameter of [**NdfExecuteDiagnosis**](ndfexecutediagnosis.md) from **NULL** to the handle (HWND) of the parent window.

This example can be modified to diagnose other areas of networking. To do so, replace the [**NdfCreateWebIncident**](ndfcreatewebincident.md) call with one of the other incident creation functions, such as [**NdfCreateDNSIncident**](ndfcreatednsincident.md) or [**NdfCreateWinSockIncident**](ndfcreatewinsockincident.md).

## Related topics

<dl> <dt>

[**NdfCloseIncident**](ndfcloseincident.md)
</dt> <dt>

[**NdfCreateWebIncident**](ndfcreatewebincident.md)
</dt> <dt>

[**NdfExecuteDiagnosis**](ndfexecutediagnosis.md)
</dt> </dl>

 

 




