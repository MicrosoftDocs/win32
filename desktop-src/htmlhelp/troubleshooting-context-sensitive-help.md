---
title: Troubleshooting Context-Sensitive Help
description: Troubleshooting Context-Sensitive Help
ms.assetid: '12E7E8C3-72B5-4a71-8A6E-BC6B2769ADD0'
---

# Troubleshooting Context-Sensitive Help

If your context-sensitive help is not working properly, use the following checklist to locate and solve the problem:

**Mapping issues**

-   Are the IDs contained in your compiled help (.chm) file mapped in your project (.hhp) file?
-   Does each ID that is mapped in the project file have a topic in the compiled help file?

**Included file issues**

-   Have you included a header (.h) file in the \[TEXT POPUPS\] section in your project (.hhp) file?
-   Have you included a text (.txt) file in the \[TEXT POPUPS\] section in your project file?
-   Is your \[TEXT POPUPS\] section referencing the correct location of the header and text files?

**Pop-up help topic issues**

-   Do the topic IDs in the text file match the symbolic IDs in the header file?
-   Have you double-checked your text file for misspellings or syntax errors?

> [!Note]  
> If you used the IDH\_ prefix for your context-sensitive help topic IDs, HTML Help Workshop automatically compares the topic IDs in your compiled help file against those mapped to numeric values in your project file. Compiler messages will tell you where your context-sensitive help is broken so you can fix it.

 

## Related topics

<dl> <dt>

[About Creating Context-Sensitive Help](create-context-sensitive-help.md)
</dt> </dl>

 

 




