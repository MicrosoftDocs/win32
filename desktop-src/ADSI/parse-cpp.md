---
title: PARSE.CPP
description: In the example provider component, a code example of the directory service path parser is in Parse.cpp.
ms.assetid: 5d68065b-0dab-41c9-baf1-f9610656bd6e
ms.tgt_platform: multiple
keywords:
- parse.cpp ADSI
- path parser ADSI
ms.topic: article
ms.date: 05/31/2018
---

# PARSE.CPP

In the example provider component, a code example of the directory service path parser is in Parse.cpp. The path parser is a key component in ADs provider components. It verifies the syntactic validity of an ADs path passed to this provider. If the syntax is valid, an **OBJECTINFO** structure is constructed, which contains a componentized version of the ADspath for this object.

Be aware that this is only a syntax verification. Rather than special-case every new iteration of path, all path verification must conform to the grammar rules established by the parser.

The following table lists the functions and methods implemented in Parse.cpp.



| Item                      | Description                                                                                                                                                            |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ADsObject**             | Parses the ADspath passed to it. This function follows the following grammar rules: &lt;ADsObject&gt; -> &lt;ProviderName&gt; &lt;SampleDSObject&gt;<br/>     |
| **SampleDSObject**        | Parses the following grammar rules: &lt;SampleDSObject&gt; -> "\\\\" &lt;identifier&gt; "\\" &lt;Pathname&gt;<br/>                                            |
| **ProviderName**          | Adds in the syntactically correct provider name if not there.                                                                                                          |
| **PathName**              | Parses the following grammar rules: &lt;Pathname&gt; -> &lt;Component&gt; "\\\\" &lt;Pathname&gt; OR<br/> &lt;Pathname&gt; -> &lt;Component&gt;<br/> |
| **Component**             | Parses the following grammar rules: &lt;Identifier&gt; OR<br/> &lt;Identifier&gt; "=" &lt;Identifier&gt;<br/>                                              |
| **CLexer::CLexer**        | Standard constructor.                                                                                                                                                  |
| **CLexer::~CLexer**       | Standard destructor.                                                                                                                                                   |
| **CLexer::GetNextToken**  | Tokenizer.                                                                                                                                                             |
| **CLexer::NextChar**      | Retrieves next single character.                                                                                                                                       |
| **CLexer::PushBackToken** | Backs up to the start of the last token.                                                                                                                               |
| **CLexer::PushbackChar**  | Backs up one character.                                                                                                                                                |
| **CLexer::IsKeyword**     | Verifies keyword list. Defined in Globals.h).                                                                                                                          |
| **AddComponent**          | Adds this component to the component array.                                                                                                                            |
| **AddProviderName**       | Adds a syntactically correct provider name to the **OBJECTINFO** structure.                                                                                            |
| **AddRootRDN**            | Adds the syntactically correct root relative distinguished name (RDN) name to the **OBJECTINFO** structure.                                                            |
| **SetType**               | Sets the type of the object.                                                                                                                                           |
| **Type**                  | Parses Type-> "user" \| "group" and so on.                                                                                                                          |



 

 

 





