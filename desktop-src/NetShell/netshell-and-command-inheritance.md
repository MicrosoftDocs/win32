---
title: NetShell and Command Inheritance
description: NetShell is designed to provide command inheritance, which means that a command valid in a given context is also valid for all of its subcontexts. For example, if a command is valid in the ras context, it is also valid in its ip and ipx subcontexts.
ms.assetid: 'b0b14217-3c99-4159-9f8b-96f90109d81c'
keywords: ["command inheritance NetSh", "components NetSh , command inheritance"]
---

# NetShell and Command Inheritance

NetShell is designed to provide command inheritance, which means that a command valid in a given context is also valid for all of its subcontexts. For example, if a command is valid in the **ras** context, it is also valid in its **ip** and **ipx** subcontexts.

Command inheritance ensures that all commands common to the NetShell root are available in all subcontexts. This enables commands that provide basic functionality such as context navigation, **popd** or **pushd** for examples, to be available in all contexts.

Common commands can be overridden in a context if another command in a context (or subcontext) is defined with the same name. For example, if **ras** has a command called **sampleping**, and the **ipx** subcontext also had a command called **sampleping** that performed a different operation, the **ipx** version of **sampleping** would override the **ras** version when a user was specifically working in the **ras ipx** subcontext.

 

 




