---
title: Container Controls
description: Container Controls
ms.assetid: 4fa59272-54b6-4da9-a7f5-e1b4eab7fa80
ms.topic: article
ms.date: 05/31/2018
---

# Container Controls

As described above, container controls are ActiveX controls that visually contain other controls. The ActiveX controls architecture specifies the [**ISimpleFrameSite**](/windows/desktop/api/OCIdl/nn-ocidl-isimpleframesite) interface to enable container controls. Containers may also support container controls without supporting **ISimpleFrameSite**, although the behavior cannot be guaranteed. For this reason, a component category exists for SimpleFrameSite controls where the full functionality of this interface is required.

To support container controls without implementing [**ISimpleFrameSite**](/windows/desktop/api/OCIdl/nn-ocidl-isimpleframesite), an ActiveX control container must:

-   Activate all controls at all times.
-   Reparent the contained controls to the hWnd of the containing control.
-   Remain the parent of the container control.

 

 




