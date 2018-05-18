---
Description: 'An application can truncate or extend a file by calling SetEndOfFile.'
ms.assetid: '23a0242d-50e9-4324-bb09-505afe383a80'
title: Truncating or Extending Files
---

# Truncating or Extending Files

An application can truncate or extend a file by calling [**SetEndOfFile**](setendoffile.md). This function sets the end-of-file marker to the current position of the file pointer.

Note that when a file is extended, the contents between the old and new end-of-file locations are not defined.

 

 



