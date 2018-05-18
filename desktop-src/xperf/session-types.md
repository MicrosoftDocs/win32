---
title: Session Types
description: Session Types
ms.assetid: 'e31baf41-dfd1-4632-9f57-4a7bd3f4dd5e'
---

# Session Types

The following two ETW session types are used to simplify the names of session and profile objects:

-   InSequentialFile sessions: These sessions are saved into a file sequentially, extending it until a preset maximum file size is reached. This behavior maps to the ETW sequential mode.

-   InBuffer sessions: These sessions save data in memory, overwriting the oldest data with the most recent data continually. They must be saved to a snapshot file for analysis. This behavior maps to the ETW buffering mode.

 

 




