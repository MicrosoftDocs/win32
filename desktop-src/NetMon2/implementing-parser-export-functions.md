---
description: The parser export functions provide all the functionality of the parsers in the parser DLL. Each parser DLL must implement ParserAutoInstallInfo and DllMain. The remaining export functions must be implemented for each parser included in the parser DLL.
ms.assetid: be73623c-7ae7-4ca9-be6c-52f513cd38a4
title: Implementing Parser Export Functions
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Parser Export Functions

The parser export functions provide all the functionality of the parsers in the parser DLL. Each parser DLL must implement [**ParserAutoInstallInfo**](parserautoinstallinfo.md) and [**DllMain**](dllmain-parser.md). The remaining export functions must be implemented for each parser included in the parser DLL.

The following topics show you how to implement the export functions.



| Term                                                                                                                                                                                                                                                   | Description                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Implementing_ParserAutoInstallInfo"></span><span id="implementing_parserautoinstallinfo"></span><span id="IMPLEMENTING_PARSERAUTOINSTALLINFO"></span>[Implementing ParserAutoInstallInfo](implementing-parserautoinstallinfo.md)<br/> | Provides a description and code example of implementing the [**ParserAutoInstallInfo**](parserautoinstallinfo.md) function, which identifies the parsers located in a parser DLL.<br/>                                                                                            |
| <span id="Implementing_DllMain_Parser"></span><span id="implementing_dllmain_parser"></span><span id="IMPLEMENTING_DLLMAIN_PARSER"></span>[Implementing DllMain Parser](implementing-dllmain-parser.md)<br/>                                    | Provides a description and code example of implementing the [**DllMain Parser**](dllmain-parser.md) function, which identifies the existence of a parser, and then releases resources that Network Monitor uses for the parser.<br/>                                              |
| <span id="Implementing_Register"></span><span id="implementing_register"></span><span id="IMPLEMENTING_REGISTER"></span>[Implementing Register](implementing-register.md)<br/>                                                                  | Provides a description and code example of implementing the [**Register**](register-parser.md) function, which records all the properties of a protocol.<br/>                                                                                                                     |
| <span id="Implementing_RecognizeFrame"></span><span id="implementing_recognizeframe"></span><span id="IMPLEMENTING_RECOGNIZEFRAME"></span>[Implementing RecognizeFrame](implementing-recognizeframe.md)<br/>                                    | Provides a description and code example of implementing the [**RecognizeFrame**](recognizeframe.md) function, which identifies an instance of a protocol in a frame.<br/>                                                                                                         |
| <span id="Implementing_AttachProperties"></span><span id="implementing_attachproperties"></span><span id="IMPLEMENTING_ATTACHPROPERTIES"></span>[Implementing AttachProperties](implementing-attachproperties.md)<br/>                          | Provides a description and code example of implementing the [**AttachProperties**](attachproperties.md) function, which separates the data that the parser recognizes, and then attaches property descriptions to each protocol property that exists in the recognized data.<br/> |
| <span id="Implementing_FormatProperties"></span><span id="implementing_formatproperties"></span><span id="IMPLEMENTING_FORMATPROPERTIES"></span>[Implementing FormatProperties](implementing-formatproperties.md)<br/>                          | Provides a description and code example of implementing the [**FormatProperties**](formatproperties.md) function, which formats the data that is displayed in the details pane of the Network Monitor UI.<br/>                                                                    |
| <span id="Implementing_Deregister"></span><span id="implementing_deregister"></span><span id="IMPLEMENTING_DEREGISTER"></span>[Implementing Deregister](implementing-deregister.md)<br/>                                                        | Provides a description and code example of implementing the [**Deregister**](deregister.md) function, which releases the resources used to register protocol properties.<br/>                                                                                                     |



 

 

 




