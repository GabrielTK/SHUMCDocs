# ⚔ Town Wars

{% hint style="danger" %}
**Players drop their inventory when they die during a war.**
{% endhint %}

**Introduction/Game-play:**

There are 6 basic types of war

* Riot - One town fighting amongst itself. Players side with the city or the rioters via team selection.
* Town vs Town - Two towns fight against each other.
* Civil War - One nation fighting amongst itself. Towns side with the capital or the rebels via team selection.
* Nation vs Nation - Two nations fight against each other.
* Alliance vs Alliance - Two nations fight against each other, with both nations' allies joining the fight.
* World War - All nations with enemies will be thrown into war. Similar to the old EventWar.

Wars are begun by an admin or via town-purchased Declaration of War books.

Declarations of War are purchased via Tokens using

```
/town redeem {wartype}
```

***

**Declaration of War Books:**

Declaration of War books are how players start wars. These books are purchased for Tokens using the `/town redeem` command. By default riots DoW books cost the least, with the costs increasing as the scopes of the wars increase as well. This means that riots and town wars will happen more often than civil wars, nation wars and world wars. A town must be a part of a nation to redeem their tokens for civil war, nation war and world wars books. It is possible for towns to purchase DoW books and then give them to other towns. This means powerful nations can foment wars in other towns to destabilize them. Declaration of War books are used by holding the book and using the `/declare war [wartype] [arg]` command, this is documented in the books themselves.

***

**TownBlock HP Sytem:**

When a war type has the TownBlockHP system enabled all of the townblocks in each warring town are given an HP amount. By default normal townblocks have 60 and homeblocks have 120 hp. HP is lowered when attackers are stood in the townblock, and the attackers outnumber any allies of the town being attacked. Optionally, townblock HPs can be healed when the allies outnumber the attackers. Townblocks must be attacked from the edge of town, inwards towards the town's homeblock. When townblocks are attacked, fireworks appear in the air above. There is a configurable minimum height that players must be in the world to be considered an attacker. If a jail plot has its HP dropped to zero, all of the prisoners of war will be unjailed in a prison break, and the jail will no longer be usable for the duration of the war. If the War allows it, TownBlocks can switch Towns when they are dropped to 0hp. See the /eventwar guide \[wartype] to learn if this is enabled on your server for TownWar, NationWar, AllianceWar or WorldWar. It is not available for Riots or CivilWars. If the War allows it and TownBlocks-can-switch-Towns is true, TownBlocks which have switched sides can be re-conquered after a configurable period of time. See the /eventwar guide \[wartype] to learn if this is enabled on your server for TownWar, NationWar, AllianceWar or WorldWar. It is not available for Riots or CivilWars.

***

**Surrendering:**

When a war type allows surrendering, players are able to decide if they can give up. For Riot, CivilWar, AllianceWar, and WorldWar types, the player uses /surrender. Riots allow for anyone to surrender. CivilWar only allows a mayor to surrender their town. WorldWar only allows a king to surrender their nation. If Riot wars have town conquering enabled, and the Mayor is the one surrendering, their Town will be taken over by the Rebel with the highest score. If CivilWar has town conquering enabled, and the King is the one surrendering, the rebel Town with the highest score will become the new Capital. For TownWar and NationWar, it is more complicated. The town or nation that wishes to give in must create an offer. This offer can be for a WhitePeace (nothing,) Money, Towns or Money & Towns combined. See '/surrender ?' for correct command syntax. The offer is then sent to the mayor or king on the opposite side for their approval. If accepted the war is over and any money or towns is exchanged. In TownWars, the surrendering Town can only offer itself in surrender, to be merged into the victorious Town. In NationWars, the surrendering Nation can offer itself or any of its Towns in surrender, to be conquered by the victorious Nation.

***

**Jails and Prisoners of War:**

EventWar makes generous use of the Towny Jail plots, players killed in enemy territory will be transferred to the town's primary jail (falling back to other jails if the primary jail has lost its HP,) to live as a POW (prisoner-of-war.) In riot wars, players are unjailed if they can leave the jail plot. In other war types they must exit the town's land. Jailbreaks occur when a jail's HP is dropped to zero and all prisoners are freed. While jailed, players are unable to score kills, lose their lives or damage townblock HP's.

***

**End conditions:**

Wars can be ended by the following conditions:

* A Riot will be ended if:
  * All of the surviving rioters are in Jail.
  * All of the players on either side run out of lives
  * The mayor is killed and mayordeath is enabled for riots.
  * The mayor surrenders, or either side's remaining players surrender.
* A town can be knocked out of a war in the following ways:
  * A town has its homeblock fall to 0hp (when the TownBlockHP system is enabled.)
  * A mayor runs out of lives and the mayordeath option is enabled for the wartype.
  * A towns' residents collectively lose all their lives.
  * A town cannot pay the death costs because their town bank has no money (when using\_economy is true.)
  * A town makes a surrender offer which is accepted.
* A nation can be knocked out of a war in the following ways:
  * A nation's king runs out of lives and mayordeath is enabled for the wartype.
  * A nation's capital city is knocked out of the war.
  * A nation's towns are all removed from the war.
  * A nation makes a surrender offer which is accepted.
* A alliance war will end if:
  * All the nations on either side are removed from the war.
* A civil war will end if:
  * The capital city is removed from the war.
  * All the towns on either side are removed from the war.
  * The king surrenders, or either side's remaining towns surrender.
* A world war will end if:
  * There is only one Nation left, or all of the remaining Nations consider each other Allies.
* Each war type has an optional, configurable max-duration, to keep wars from going on indefinitely.

***

**Commands:**

* **/eventwar**
  * **/eventwar guide:** Opens a book for the player, explaining how EventWar works, based on your server's config settings.
  * **/eventwar guide riot:** Opens a book for the player, explaining riots.
  * **/eventwar guide townwar:** Opens a book for the player, explaining town vs town wars.
  * **/eventwar guide civilwar:** Opens a book for the player, explaining civil wars.
  * **/eventwar guide nationwar:** Opens a book for the player, explaining nation wars.
  * **/eventwar guide alliancewar:** Opens a book for the player, explaining alliance wars.
  * **/eventwar guide worldwar:** Opens a book for the player, explaining world wars.
  * **/eventwar guide conquering:** Opens a book for the player, explaining how conquering works.
  * **/eventwar guide townblocks:** Opens a book for the player, explaining how the TownBlock HP system works.
  * **/eventwar guide money:** Opens a book for the player, explaining how money affects wars.
  * **/eventwar guide winning:** Opens a book for the player, explaining how to win wars.
  * **/eventwar guide points:** Opens a book for the player, explaining how points are scored.
  * **/eventwar guide jails:** Opens a book for the player, explaining how jails and PoWs work.
* **/towny war**
  * **/towny war hud:** Opens a scoreboard for the player, which details points and properties of the townblock they are standing in.
  * **/towny war participants {page #}:** A list of towns and their nation who are in each on-going war. The list highlights enemies, allies and capital towns. While war is in effect, each competing town has a health points property attached to it.
  * **/towny war stats:** Shows stats on the player's current war.
  * **/towny war scores:** Shows the scores of the player's current war.
  * **/towny war types:** Shows the settings of various war types (mainly for debugging now.)
* **/town**
  * **/town redeem {wartype}:** Used to purchase a Declaration of War of the given war type.
* **/declare**
  * **/declare rebel:** Used to side with the rioters/rebels in Riot and Civil Wars.
  * **/declare government:** Used to side with the city/capital in Riot and Civil Wars.
  * **/declare war {wartype} {args}:** Used while holding a Declaration of War book of the given war type, to start a war.
* **/surrender**
  * **/surrender:** Used to surrender in Riots, Civil Wars, Alliance Wars, and World Wars.
  * **/surrender money {amount}:** Used in Town and Nation Wars to surrender for money.
  * **/surrender towns {town1 town2 town3}:** Used in Town and Nation Wars to surrender for towns.
  * **/surrender money {amount} towns {town1 town2 town3}:** Used in Town and Nation Wars to surrender for money and towns.
