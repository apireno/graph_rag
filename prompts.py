# Copyright (c) 2024 
# Modified from Microsoft Template file in the GraphRag repository
# Licensed under the MIT License

"""A file containing prompts definition."""

GRAPH_EXTRACTION_PROMPT = """
-Goal-
Given a text document that is potentially relevant to this activity and a list of entity types, identify all entities of those types from the text and all relationships among the identified entities.
 
-Steps-
1. Identify all entities. For each identified entity, extract the following information:
- entity_name: Name of the entity, capitalized
- entity_type: One of the following types: [{entity_types}]
- entity_description: Comprehensive description of the entity's attributes and activities
Format each entity as CREATE <entity_type>:`<entity_name>` SET description="<entity_description>"
 
2. From the entities identified in step 1, identify all pairs of (source_entity, target_entity) that are *clearly related* to each other.
For each pair of related entities, extract the following information:
- source_entity: name of the source entity, as identified in step 1
- target_entity: name of the target entity, as identified in step 1
- relationship_description: explanation as to why you think the source entity and the target entity are related to each other
- relationship_strength: a numeric score indicating strength of the relationship between the source entity and target entity
 Format each relationship as RELATE <source_entity_type>:`<source_entity>`->{relation_type}-><target_entity_type>:`<target_entity>` SET description="<relationship_description>", strength=<relationship_strength>
 
3. Return output in English as a single list of all the entities and relationships identified in steps 1 and 2. Use **{record_delimiter}** as the list delimiter.
 
4. When finished, output {completion_delimiter}
 
######################
-Examples-
######################
Example 1:
Entity_types: ORGANIZATION,PERSON
Text:
The Verdantis's Central Institution is scheduled to meet on Monday and Thursday, with the institution planning to release its latest policy decision on Thursday at 1:30 p.m. PDT, followed by a press conference where Central Institution Chair Martin Smith will take questions. Investors expect the Market Strategy Committee to hold its benchmark interest rate steady in a range of 3.5%-3.75%.
######################
Output:
CREATE ORGANIZATION:`CENTRAL INSTITUTION` SET description="The Central Institution is the Federal Reserve of Verdantis, which is setting interest rates on Monday and Thursday"{record_delimiter}
CREATE PERSON:`MARTIN SMITH` SET description="Martin Smith is the chair of the Central Institution"{record_delimiter}
CREATE ORGANIZATION:`MARKET STRATEGY COMMITTEE` SET description="The Central Institution committee makes key decisions about interest rates and the growth of Verdantis's money supply)"{record_delimiter}
RELATE PERSON:`MARTIN SMITH`->{relation_type}->ORGANIZATION:`CENTRAL INSTITUTION` SET description="Martin Smith is the Chair of the Central Institution and will answer questions at a press conference", strength=9{record_delimiter}
{completion_delimiter}

######################
Example 2:
Entity_types: ORGANIZATION
Text:
TechGlobal's (TG) stock skyrocketed in its opening day on the Global Exchange Thursday. But IPO experts warn that the semiconductor corporation's debut on the public markets isn't indicative of how other newly listed companies may perform.

TechGlobal, a formerly public company, was taken private by Vision Holdings in 2014. The well-established chip designer says it powers 85% of premium smartphones.
######################
Output:
CREATE ORGANIZATION:`TECHGLOBAL` SET description="TechGlobal is a stock now listed on the Global Exchange which powers 85% of premium smartphones"{record_delimiter}
CREATE ORGANIZATION:`VISION HOLDINGS` SET description="Vision Holdings is a firm that previously owned TechGlobal"{record_delimiter}
RELATE ORGANIZATION:`TECHGLOBAL` ->{relation_type}->ORGANIZATION:`VISION HOLDINGS` SET description = "Vision Holdings formerly owned TechGlobal from 2014 until present", strength=5{record_delimiter}
{completion_delimiter}

######################
Example 3:
Entity_types: ORGANIZATION,GEO,PERSON
Text:
Five Aurelians jailed for 8 years in Firuzabad and widely regarded as hostages are on their way home to Aurelia.

The swap orchestrated by Quintara was finalized when $8bn of Firuzi funds were transferred to financial institutions in Krohaara, the capital of Quintara.

The exchange initiated in Firuzabad's capital, Tiruzia, led to the four men and one woman, who are also Firuzi nationals, boarding a chartered flight to Krohaara.

They were welcomed by senior Aurelian officials and are now on their way to Aurelia's capital, Cashion.

The Aurelians include 39-year-old businessman Samuel Namara, who has been held in Tiruzia's Alhamia Prison, as well as journalist Durke Bataglani, 59, and environmentalist Meggie Tazbah, 53, who also holds Bratinas nationality.
######################
Output:
CREATE GEO:`FIRUZABAD` SET description="Firuzabad held Aurelians as hostages"{record_delimiter}
CREATE GEO:`AURELIA` SET description="Country seeking to release hostages"{record_delimiter}
CREATE GEO:`QUINTARA` SET description="Country that negotiated a swap of money in exchange for hostages"{record_delimiter}
CREATE GEO:`TIRUZIA` SET description="Capital of Firuzabad where the Aurelians were being held"{record_delimiter}
CREATE GEO:`KROHAARA` SET description="Capital city in Quintara"{record_delimiter}
CREATE GEO:`CASHION` SET description="Capital city in Aurelia"{record_delimiter}
CREATE PERSON:`SAMUEL NAMARA` SET description="Aurelian who spent time in Tiruzia's Alhamia Prison"{record_delimiter}
CREATE GEO:`ALHAMIA PRISON` SET description="Prison in Tiruzia"{record_delimiter}
CREATE PERSON:`DURKE BATAGLANI` SET description="Aurelian journalist who was held hostage"{record_delimiter}
CREATE PERSON:`MEGGIE TAZBAH` SET description="Bratinas national and environmentalist who was held hostage"{record_delimiter}


RELATE GEO:`FIRUZABAD`->{relation_type}->GEO:`AURELIA` SET description="Firuzabad negotiated a hostage exchange with Aurelia", strength=2{record_delimiter}
RELATE GEO:`QUINTARA`->{relation_type}->GEO:`AURELIA` SET description="Quintara brokered the hostage exchange between Firuzabad and Aurelia", strength=2{record_delimiter}
RELATE GEO:`QUINTARA`->{relation_type}->GEO:`FIRUZABAD` SET description="Quintara brokered the hostage exchange between Firuzabad and Aurelia", strength=2{record_delimiter}
RELATE PERSON:`SAMUEL NAMARA`->{relation_type}->GEO:`ALHAMIA PRISON` SET description="Samuel Namara was a prisoner at Alhamia prison", strength=8{record_delimiter}
RELATE PERSON:`SAMUEL NAMARA`->{relation_type}->PERSON:`MEGGIE TAZBAH` SET description="Samuel Namara and Meggie Tazbah were exchanged in the same hostage release", strength=2{record_delimiter}
RELATE PERSON:`SAMUEL NAMARA>`->{relation_type}->PERSON:`DURKE BATAGLANI` SET description="Samuel Namara and Durke Bataglani were exchanged in the same hostage release", strength=2{record_delimiter}
RELATE PERSON:`MEGGIE TAZBAH`->{relation_type}->PERSON:`DURKE BATAGLANI` SET description="Meggie Tazbah and Durke Bataglani were exchanged in the same hostage release", strength=2{record_delimiter}
RELATE PERSON:`SAMUEL NAMARA`->{relation_type}->GEO:`FIRUZABAD` SET description="Samuel Namara was a hostage in Firuzabad", strength=2{record_delimiter}
RELATE PERSON:`MEGGIE TAZBAH`->{relation_type}->GEO:`FIRUZABAD` SET description="Meggie Tazbah was a hostage in Firuzabad", strength=2{record_delimiter}
RELATE PERSON:`DURKE BATAGLANI`->{relation_type}->GEO:`FIRUZABAD` SET description="Durke Bataglani was a hostage in Firuzabad", strength=2{record_delimiter}
{completion_delimiter}

######################
-Real Data-
######################
Entity_types: {entity_types}
Text: {input_text}
######################
Output:"""

CONTINUE_PROMPT = "MANY entities and relationships were missed in the last extraction. Try to identify relationships that may be weaker or were not apparent at your first attempt. Make sure to have at least one relationship for each entity even if it is to itself. AND make sure to add any entities mentioned in relationships. Remember to ONLY emit entities that match any of the previously extracted types and do NOT extract the entities from the examples sections. Add them below using the same format. Do not add any explanatory text outside of the instructions you were given as the OUTPUT. If you cannot find any more relationships after trying very hard then return only the completion delimiter: {completion_delimiter}.\n"
LOOP_PROMPT = "It appears some entities and relationships may have still been missed.  Answer YES | NO if there are still entities or relationships that need to be added. ONLY answer with 'YES' or 'NO' and nothing else!\n"



