---
title: IUpdateOrchestratorActionCallback::ReportCompleted method
description: Called when the action is complete and has not failed.
ms.date: 12/01/2020
ms.topic: method
---

# IUpdateOrchestratorActionCallback::ReportCompleted method

Called when the action is complete and has not failed.

## Syntax
```cpp
HRESULT ReportCompleted();
```

## Returns
If this method succeeds, it returns S_OK. Otherwise, it returns an HRESULT error code.

## See Also

[IUpdateOrchestratorActionCallback](iupdateorchestratoractioncallback.md)

[IUpdateOrchestratorActionCallback::ReportFailed](iupdateorchestratoractioncallback-reportfailed.md)

[IUpdateOrchestratorActionCallback::ReportProgress](iupdateorchestratoractioncallback-reportprogress.md)