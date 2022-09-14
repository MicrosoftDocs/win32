---
description: Setting the Error Log
ms.assetid: 2e3124e3-32d0-4eb6-9c1d-91b625018ac4
title: Setting the Error Log
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Error Log

\[This API is not supported and may be altered or unavailable in the future.\]

After you implement the error logging class, create a new instance of the class. Then, give [DirectShow Editing Services](directshow-editing-services.md) a pointer to it by calling the [**IAMSetErrorLog::put\_ErrorLog**](iamseterrorlog-put-errorlog.md) method on the timeline. Query the timeline for the **IAMSetErrorLog** interface. To ensure that all errors are logged, you should call this method before you load, save, or render the timeline.


```C++
IAMSetErrorLog  *pSetLog = NULL;
IAMErrorLog     *pLog = new CErrReporter();

pTL->QueryInterface(IID_IAMSetErrorLog, (void **)&pSetLog);
pSetLog->put_ErrorLog(pLog);
pSetLog->Release();
```



Error logging has no effect on the return values that you receive when you call methods in your application. Error logging complements but does not replace the usual error handling techniques. To create a robust application, always check HRESULT values.

## Related topics

<dl> <dt>

[Logging Errors](logging-errors.md)
</dt> </dl>

 

 



