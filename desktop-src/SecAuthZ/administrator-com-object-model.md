---
description: An application running as a standard user performs operations that require administrator privilege by creating an elevated Component Object Model object.
ms.assetid: 246fdf74-cc5b-47b1-b3a8-20441544e7be
title: Administrator COM Object Model
ms.topic: article
ms.date: 05/31/2018
---

# Administrator COM Object Model

In the administrator COM object model, an application running as a standard user performs operations that require administrator privilege by creating an elevated [Component Object Model](/windows/desktop/com/component-object-model--com--portal) object. For information about creating an elevated COM object, see [The COM Elevation Moniker](../com/the-com-elevation-moniker.md).

One drawback to using the administrator COM object model is that the user is prompted each time a privileged operation is performed.

Any user interface that can control the COM object must be presented by the COM object itself. Otherwise, an unprivileged process could cause the elevated COM object to perform privileged operations without the user being prompted.

## Related topics

<dl> <dt>

[Developing Applications that Require Administrator Privilege](developing-applications-that-require-administrator-privilege.md)
</dt> <dt>

[Administrator Broker Model](administrator-broker-model.md)
</dt> <dt>

[Elevated Task Model](elevated-task-model.md)
</dt> <dt>

[Operating System Service Model](operating-system-service-model.md)
</dt> </dl>

 

 
