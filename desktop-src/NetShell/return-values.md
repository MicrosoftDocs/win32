---
title: Return Values
description: A helper command issued from inside NetShell should return whether the operation succeeded or failed. For example, a helper should return NO\_ERROR for success and ERROR\_SUPPRESS\_OUTPUT for failure.
ms.assetid: '698976d5-60a7-4dbb-a6d0-1cf42dd4f94a'
---

# Return Values

A helper command issued from inside NetShell should return whether the operation succeeded or failed. For example, a helper should return **NO\_ERROR** for success and **ERROR\_SUPPRESS\_OUTPUT** for failure.

If the helper requires NetShell to print more detailed failure responses, the helper should return **ERROR\_OKAY** for success, and descriptive error values for failure, for example, **ERROR\_INSUFFICENT\_MEMORY**.

 

 




