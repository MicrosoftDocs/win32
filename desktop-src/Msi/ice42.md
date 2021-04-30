---
description: ICE42 validates that InProc servers are not linked to EXE files in the Class table. It also validates that only LocalServer and LocalServer32 classes have arguments and DefInProc values.
ms.assetid: 14976772-c873-46d8-8687-dcdad2420d83
title: ICE42
ms.topic: article
ms.date: 05/31/2018
---

# ICE42

ICE42 validates that InProc servers are not linked to EXE files in the [Class table](class-table.md). It also validates that only LocalServer and LocalServer32 classes have arguments and DefInProc values.

## Result

ICE42 posts an error if there are InProc servers linked to EXE files in the Class table.

## Example

ICE42 would report the following errors for the example shown.



| ICE42 error                                                                                                                             | Description                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CLSID '{GUID1}' is an InProc server, but the implementing component 'Component1' has an EXE ('test.exe') as its KeyFile.                | There is an executable file specified as an InProc server. EXE files cannot be InProc servers.                                                                                                                            |
| CLSID '{GUID1}' in context 'InProcServer32' has an argument. Only LocalServer contexts can have arguments.                              | To fix this error, remove the argument.                                                                                                                                                                                   |
| CLSID '{GUID1}' in context 'InProcServer32' specifies a default InProc value. Only LocalServer contexts can have default InProc values. | There is an object with a default InProc value that is not an object operating in the LocalServer or LocalServer32 contexts. To fix this error, remove the DeflnProc value or change the context of the class.<br/> |



 

[Class Table](class-table.md) (partial)



| CLSID   | Context        | Component\_ | DefInProcHandler | Argument |
|---------|----------------|-------------|------------------|----------|
| {GUID1} | InProcServer32 | Component1  | InProcServer     | Arg      |



 

[Component Table](component-table.md) (partial)



| Component  | KeyPath |
|------------|---------|
| Component1 | File1   |



 

[File Table](file-table.md) (partial)



| File  | Filename |
|-------|----------|
| File1 | test.exe |



 

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 




