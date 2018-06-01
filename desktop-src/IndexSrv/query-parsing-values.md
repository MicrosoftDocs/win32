---
Description: Values 0xHHHH1650 to 0xHHHH167F are query-return values produced by utilities in query.lib. The following table gives the query-parsing values in alphabetical order.
ms.assetid: ecb7a343-6921-49b8-8b31-717370787e6f
title: Query-Parsing Values
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Query-Parsing Values

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Values 0x*HHHH*1650 to 0x*HHHH*167F are query-return values produced by utilities in query.lib. The following table gives the query-parsing values in alphabetical order.



| Constant/value                                                                                                                                                                                                                                                                                      | Description                                                                                              |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| <span id="QPARSE_E_EXPECTING_BRACE"></span><span id="qparse_e_expecting_brace"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_BRACE**</dt> <dt>0x80041666</dt> </dl>                                    | Expecting closing square bracket '\]'.<br/>                                                        |
| <span id="QPARSE_E_EXPECTING_COMMA"></span><span id="qparse_e_expecting_comma"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_COMMA**</dt> <dt>0x80041671</dt> </dl>                                    | Expecting comma.<br/>                                                                              |
| <span id="QPARSE_E_EXPECTING_CURRENCY"></span><span id="qparse_e_expecting_currency"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_CURRENCY**</dt> <dt>0x80041664</dt> </dl>                           | Expecting currency.<br/>                                                                           |
| <span id="QPARSE_E_EXPECTING_DATE"></span><span id="qparse_e_expecting_date"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_DATE**</dt> <dt>0x80041663</dt> </dl>                                       | Expecting date.<br/>                                                                               |
| <span id="QPARSE_E_EXPECTING_EOS"></span><span id="qparse_e_expecting_eos"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_EOS**</dt> <dt>0x80041670</dt> </dl>                                          | Expecting end of string.<br/>                                                                      |
| <span id="QPARSE_E_EXPECTING_GUID"></span><span id="qparse_e_expecting_guid"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_GUID**</dt> <dt>0x80041665</dt> </dl>                                       | Expecting GUID.<br/>                                                                               |
| <span id="QPARSE_E_EXPECTING_INTEGER"></span><span id="qparse_e_expecting_integer"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_INTEGER**</dt> <dt>0x80041661</dt> </dl>                              | Expecting integer.<br/>                                                                            |
| <span id="QPARSE_E_EXPECTING_PAREN"></span><span id="qparse_e_expecting_paren"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_PAREN**</dt> <dt>0x80041667</dt> </dl>                                    | Expecting closing parenthesis ')'.<br/>                                                            |
| <span id="QPARSE_E_EXPECTING_PHRASE"></span><span id="qparse_e_expecting_phrase"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_PHRASE**</dt> <dt>0x8004166A</dt> </dl>                                 | Expecting phrase.<br/>                                                                             |
| <span id="QPARSE_E_EXPECTING_PROPERTY"></span><span id="qparse_e_expecting_property"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_PROPERTY**</dt> <dt>0x80041668</dt> </dl>                           | Expecting property name.<br/>                                                                      |
| <span id="QPARSE_E_EXPECTING_REAL"></span><span id="qparse_e_expecting_real"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_REAL**</dt> <dt>0x80041662</dt> </dl>                                       | Expecting real number.<br/>                                                                        |
| <span id="QPARSE_E_EXPECTING_REGEX"></span><span id="qparse_e_expecting_regex"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_REGEX**</dt> <dt>0x8004166C</dt> </dl>                                    | Expecting regular expression.<br/>                                                                 |
| <span id="QPARSE_E_EXPECTING_REGEX_PROPERTY"></span><span id="qparse_e_expecting_regex_property"></span><dl> <dt>**QPARSE\_E\_EXPECTING\_REGEX\_PROPERTY**</dt> <dt>0x8004166D</dt> </dl>        | Regular expressions require a property of type string.<br/>                                        |
| <span id="QPARSE_E_INVALID_GROUPING"></span><span id="qparse_e_invalid_grouping"></span><dl> <dt>**QPARSE\_E\_INVALID\_GROUPING**</dt> <dt>0x80041677</dt> </dl>                                 | An unsupported grouping type was specified.<br/>                                                   |
| <span id="QPARSE_E_INVALID_LITERAL"></span><span id="qparse_e_invalid_literal"></span><dl> <dt>**QPARSE\_E\_INVALID\_LITERAL**</dt> <dt>0x8004166E</dt> </dl>                                    | Invalid literal.<br/>                                                                              |
| <span id="QPARSE_E_INVALID_QUERY"></span><span id="qparse_e_invalid_query"></span><dl> <dt>**QPARSE\_E\_INVALID\_QUERY**</dt> <dt>0x8004167A</dt> </dl>                                          | Invalid query.<br/>                                                                                |
| <span id="QPARSE_E_INVALID_RANKMETHOD"></span><span id="qparse_e_invalid_rankmethod"></span><dl> <dt>**QPARSE\_E\_INVALID\_RANKMETHOD**</dt> <dt>0x8004167BL</dt> </dl>                          | Invalid rank method.<br/>                                                                          |
| <span id="QPARSE_E_INVALID_SORT_ORDER"></span><span id="qparse_e_invalid_sort_order"></span><dl> <dt>**QPARSE\_E\_INVALID\_SORT\_ORDER**</dt> <dt>0x80041675</dt> </dl>                          | An invalid sort order was specified. Only \[a\] and \[d\] are supported.<br/>                      |
| <span id="QPARSE_E_NO_SUCH_PROPERTY"></span><span id="qparse_e_no_such_property"></span><dl> <dt>**QPARSE\_E\_NO\_SUCH\_PROPERTY**</dt> <dt>0x8004166F</dt> </dl>                                | No such property.<br/>                                                                             |
| <span id="QPARSE_E_NO_SUCH_SORT_PROPERTY"></span><span id="qparse_e_no_such_sort_property"></span><dl> <dt>**QPARSE\_E\_NO\_SUCH\_SORT\_PROPERTY**</dt> <dt>0x80041674</dt> </dl>                | An invalid property was found in the sort specification.<br/>                                      |
| <span id="QPARSE_E_NOT_YET_IMPLEMENTED"></span><span id="qparse_e_not_yet_implemented"></span><dl> <dt>**QPARSE\_E\_NOT\_YET\_IMPLEMENTED**</dt> <dt>0x80041669</dt> </dl>                       | Not yet implemented.<br/>                                                                          |
| <span id="QPARSE_E_UNEXPECTED_EOS"></span><span id="qparse_e_unexpected_eos"></span><dl> <dt>**QPARSE\_E\_UNEXPECTED\_EOS**</dt> <dt>0x80041672</dt> </dl>                                       | Unexpected end of string.<br/>                                                                     |
| <span id="QPARSE_E_UNEXPECTED_NOT"></span><span id="qparse_e_unexpected_not"></span><dl> <dt>**QPARSE\_E\_UNEXPECTED\_NOT**</dt> <dt>0x80041660</dt> </dl>                                       | Unexpected NOT operator.<br/>                                                                      |
| <span id="QPARSE_E_UNSUPPORTED_PROPERTY_TYPE"></span><span id="qparse_e_unsupported_property_type"></span><dl> <dt>**QPARSE\_E\_UNSUPPORTED\_PROPERTY\_TYPE**</dt> <dt>0x8004166BL</dt> </dl>    | Unsupported property type.<br/>                                                                    |
| <span id="QPARSE_E_WEIGHT_OUT_OF_RANGE"></span><span id="qparse_e_weight_out_of_range"></span><dl> <dt>**QPARSE\_E\_WEIGHT\_OUT\_OF\_RANGE**</dt> <dt>0x80041673</dt> </dl>                      | Weight must be between 0 and 1000.<br/>                                                            |
| <span id="QPLIST_E_BAD_GUID"></span><span id="qplist_e_bad_guid"></span><dl> <dt>**QPLIST\_E\_BAD\_GUID**</dt> <dt>0x80041659</dt> </dl>                                                         | Invalid GUID.<br/>                                                                                 |
| <span id="QPLIST_E_BYREF_USED_WITHOUT_PTRTYPE"></span><span id="qplist_e_byref_used_without_ptrtype"></span><dl> <dt>**QPLIST\_E\_BYREF\_USED\_WITHOUT\_PTRTYPE**</dt> <dt>0x8004165E</dt> </dl> | DBTYPE\_BYREF must be used with DBTYPE\_STR, DBTYPE\_WSTR, DBTYPE\_GUID or DBTYPE\_UI1 types.<br/> |
| <span id="QPLIST_E_CANT_OPEN_FILE"></span><span id="qplist_e_cant_open_file"></span><dl> <dt>**QPLIST\_E\_CANT\_OPEN\_FILE**</dt> <dt>0x80041651</dt> </dl>                                      | Cannot open file.<br/>                                                                             |
| <span id="QPLIST_E_CANT_SET_PROPERTY"></span><span id="qplist_e_cant_set_property"></span><dl> <dt>**QPLIST\_E\_CANT\_SET\_PROPERTY**</dt> <dt>0x8004165B</dt> </dl>                             | Failed to set property name.<br/>                                                                  |
| <span id="QPLIST_E_DUPLICATE"></span><span id="qplist_e_duplicate"></span><dl> <dt>**QPLIST\_E\_DUPLICATE**</dt> <dt>0x8004165C</dt> </dl>                                                       | Duplicate property name.<br/>                                                                      |
| <span id="QPLIST_E_EXPECTING_CLOSE_PAREN"></span><span id="qplist_e_expecting_close_paren"></span><dl> <dt>**QPLIST\_E\_EXPECTING\_CLOSE\_PAREN**</dt> <dt>0x80041657</dt> </dl>                 | Expecting closing parenthesis.<br/>                                                                |
| <span id="QPLIST_E_EXPECTING_GUID"></span><span id="qplist_e_expecting_guid"></span><dl> <dt>**QPLIST\_E\_EXPECTING\_GUID**</dt> <dt>0x80041658</dt> </dl>                                       | Expecting GUID.<br/>                                                                               |
| <span id="QPLIST_E_EXPECTING_INTEGER"></span><span id="qplist_e_expecting_integer"></span><dl> <dt>**QPLIST\_E\_EXPECTING\_INTEGER**</dt> <dt>0x80041656</dt> </dl>                              | Expecting integer.<br/>                                                                            |
| <span id="QPLIST_E_EXPECTING_NAME"></span><span id="qplist_e_expecting_name"></span><dl> <dt>**QPLIST\_E\_EXPECTING\_NAME**</dt> <dt>0x80041653</dt> </dl>                                       | Expecting property name.<br/>                                                                      |
| <span id="QPLIST_E_EXPECTING_PROP_SPEC"></span><span id="qplist_e_expecting_prop_spec"></span><dl> <dt>**QPLIST\_E\_EXPECTING\_PROP\_SPEC**</dt> <dt>0x8004165A</dt> </dl>                       | Expecting property specifier.<br/>                                                                 |
| <span id="QPLIST_E_EXPECTING_TYPE"></span><span id="qplist_e_expecting_type"></span><dl> <dt>**QPLIST\_E\_EXPECTING\_TYPE**</dt> <dt>0x80041654</dt> </dl>                                       | Expecting type specifier.<br/>                                                                     |
| <span id="QPLIST_E_READ_ERROR"></span><span id="qplist_e_read_error"></span><dl> <dt>**QPLIST\_E\_READ\_ERROR**</dt> <dt>0x80041652</dt> </dl>                                                   | Read error in file.<br/>                                                                           |
| <span id="QPLIST_E_UNRECOGNIZED_TYPE"></span><span id="qplist_e_unrecognized_type"></span><dl> <dt>**QPLIST\_E\_UNRECOGNIZED\_TYPE**</dt> <dt>0x80041655</dt> </dl>                              | Unrecognized type.<br/>                                                                            |
| <span id="QPLIST_E_VECTORBYREF_USED_ALONE"></span><span id="qplist_e_vectorbyref_used_alone"></span><dl> <dt>**QPLIST\_E\_VECTORBYREF\_USED\_ALONE**</dt> <dt>0x8004165D</dt> </dl>              | DBTYPE\_VECTOR or DBTYPE\_BYREF used alone.<br/>                                                   |
| <span id="QPLIST_S_DUPLICATE"></span><span id="qplist_s_duplicate"></span><dl> <dt>**QPLIST\_S\_DUPLICATE**</dt> <dt>0x00041679</dt> </dl>                                                       | Exact duplicate property defined.<br/>                                                             |
| <span id="QUTIL_E_CANT_CONVERT_VROOT"></span><span id="qutil_e_cant_convert_vroot"></span><dl> <dt>**QUTIL\_E\_CANT\_CONVERT\_VROOT**</dt> <dt>0x80041676</dt> </dl>                             | Couldn't convert a virtual path to a physical path.<br/>                                           |
| <span id="QUTIL_E_INVALID_CODEPAGE"></span><span id="qutil_e_invalid_codepage"></span><dl> <dt>**QUTIL\_E\_INVALID\_CODEPAGE**</dt> <dt>0x80041678</dt> </dl>                                    | Invalid CiCodepage variable was specified.<br/>                                                    |



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| Header<br/>                   | <dl> <dt>Cierror.h</dt> </dl> |



 

 




