---
title: IReconcileInitiator interface
description: Exposes methods that provide the briefcase reconciler with the means to notify the initiator of its progress, to set a termination object, and to request a given version of a document. The initiator is responsible for implementing this interface.
ms.assetid: 1a32d67f-1ddc-49dc-af88-b8c41a50ac54
keywords:
- IReconcileInitiator interface Legacy Windows Environment Features
- IReconcileInitiator interface Legacy Windows Environment Features , described
topic_type:
- apiref
api_name:
- IReconcileInitiator
api_location:
- Shell32.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IReconcileInitiator interface

Exposes methods that provide the briefcase reconciler with the means to notify the initiator of its progress, to set a termination object, and to request a given version of a document. The initiator is responsible for implementing this interface.

## Members

The **IReconcileInitiator** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IReconcileInitiator** also has these types of members:

-   [Methods](#methods)

### Methods

The **IReconcileInitiator** interface has these methods.



| Method                                                                 | Description                                                                                                                                                                                                                                                                                                             |
|:-----------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetAbortCallback**](/windows/win32/api/reconcil/nf-reconcil-ireconcileinitiator-setabortcallback)       | Sets the object through which the initiator can asynchronously terminate a reconciliation. A briefcase reconciler typically sets this object for reconciliations that are lengthy or involve user interaction. <br/>                                                                                              |
| [**SetProgressFeedback**](/windows/win32/api/reconcil/nf-reconcil-ireconcileinitiator-setprogressfeedback) | Indicates the amount of progress the briefcase reconciler has made toward completing the reconciliation. The amount is a fraction and is computed as the quotient of the *ulProgress* and *ulProgressMax* parameters. Reconcilers should call this method periodically during their reconciliation process. <br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.0 or later)</dt> </dl> |



 

