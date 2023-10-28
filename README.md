# Octan Reputation Ranking System
Inspired by Google's PageRank, Octan Labs wants to build a similar system in Web3 space, namely Reputation Ranking System to helps
- Unify user data & reputation on multiple chains, then provides efficient metrics for new projects to qualify & classify potential users 
- Recognize all stakeholders, users & contributors by both staking & reputation weights, making DAOs more decentralized & democratic against staking-centrality
- Provide credibility scoring to unleash under-collateral crypto lending.

Preliminary ranking concepts:
- A node means an account (or public address) on a blockchain. It may be a personal account or a contract address.
- An edge indicates one or many directed transactions from account A to account B. 
- A (directed) graph consists of nodes and edges, presenting onchain transactions among accounts, i.e their inter-relationships.

Reputation Ranking System (RRS) typically computes reputation scores or ranking scores of all accounts in a blockchain-based transactional graph.
Octan defines three following schemas when computing reputation scores:
- *Global Reputation or Global Ranking* considers all acounts and transactions on a blockchain, for example, entirely on Ethereum (more than 200 million accounts and multi-billions of transactions between them since the genesis block). However, due to limitation in computing resources, we may restrict to most recently blocks within a deterministic timeframe, for instance, a range of all blocks from 00:00:01' Jan 1st, 2020 to 24:00:00' October 30st, 2022.   Global ranking score represents reputation or importance measurement of an account in the entire blockchain network.
- *Local/Category Reputation* considers subgraphs, i.e. sets of acounts and transactions filtered by specific (localized) criteria, for example, all transactions belonging to a token-contract (e.g. USDT), all accounts and transactions going throught Uniswap protocol or participating in DeFi markets. Local ranking score represents reputation or importance measurement of an account within a subspace of a blockchain network (currently, Octan consifers 5 subspace categories: DeFi, DAO, NFT, gamefi, socialfi).
- *Personalized/Project-based Reputation* computes reputation score of accounts relevant to one or many specific accounts, for example, a token-contract (e.g. USDT), to Uniswap protocol or to Axie Infinity game. Pertionalized ranking is similar to but not same as local ranking. It represents reputation or importance measurement of an account to one or many specific accounts.

# Reputation Ranking Algorithms  
The Octan's founder and core team have studied onchain reputation ranking problem since 2019, then introduced several adaptive PageRank algorithms to compute reputation scores from onchain transactions. List of published, peer-reviewed scientific articles on globally recognized journals and conferences:  
- 2019: Delegated Proof of Reputation: a Novel Blockchain Consensus, https://dl.acm.org/doi/abs/10.1145/3343147.3343160
- 2022: PageRank and HodgeRank on Ethereum Transactions: A Measure for Social Credit, https://www.igi-global.com/article/pagerank-and-hodgerank-on-ethereum-transactions/315737  
- 2023: On-Chain Reputation Ranking by Adaptive Weighted PageRank, accepted for the 2023 RIVF International Conference on Computing and Communication Technologies.

# Reputation Board 
Users can browse reputation ranks, scores and onchain statistics of any onchain entities (e.g. contracts or individual wallets).  
Reputation board for NEO can be found here https://octan.network/?page=1  

# Usecases of Octan RRS:
Octan RRS extracts interelation between accounts, dapps, social insights and user behaviors from onchain transactions, then provides a comprehensive score and multi-dimentional insights over a blockchain, including both idividual wallets of users and contract accounts of dapps. Therefore, Octan RRS has wide ranges of applications.
- Web3 users can use Octan RRS as a proof of Trustworthiness. They mint Octan Soulbound Token to carry, update their reputation scores, then prove their trustworthiness (visit audited Octan Soulbound token contracts https://github.com/Octan-Labs/Octan1ID-SoulBound).
- Projects and marketing agency can use Octan reputation scores as a universal metric to qualify, classify and segment users, then efficiently filtering bots or cloned accounts and targeting Web3 audiences better for airdrop/retro campaigns, loyalty program. Higher reputation score, higher user quality.  
- Researchers and investors use Octan reputation ranking as a quality measurement when evaluating projects. Higher reputation scores of the project and its average users, better the project is.
- Lenders can use reputation scores as a credibility indicator for under-collateralized loans.

Visit Octan reputation ranking reports and blogs https://blog.octan.network/. 

# Data processing pipeline
Octan has developed a data processing pipeline for Ethereum, BNB Chain and other EVM-compatible chains to serve Reputation Ranking System here https://github.com/Octan-Labs/pipeline. The pipeline processes onchain data, then provides data-inputs for reputation ranking system and warehouse to build an onchain analytics platform.  

# Octan Soulbound 
Octan develops a Soulbound token standard to unify and carry users' reputation scores accross multiple chains.  
Visit audited Octan Soulbound contracts https://github.com/Octan-Labs/Octan1ID-SoulBound)  
Mint Octan SBT (on BNB Chain mainnet) to carry and update reputation scores: https://octan.network/1-id  
We deployed Octan Soulbound and reputation contracts on NEO-EVM testnet. Whenever, the NEO-EVM mainnet is ready, we will deploy and release production, allow Web3 users to mint and update reputation scores (even from other blockchains) on NEO-EVM as proof of their trustworthiness and onchain contribution.     
- Management: https://evm.ngd.network/address/0xeb67683da8C22Aa80B2A4bB3331EAa2DBad6Fe71/contracts#address-tabs
- Reputation: https://evm.ngd.network/address/0x471a924A47F9E968aE6DBF822d9d76a0fd731993/contracts#address-tabs
- Minter: https://evm.ngd.network/address/0x48d4591D726232DA353fa315BBeC707211A774A4/contracts#address-tabs
- Updater: https://evm.ngd.network/address/0x7948DEf047b7d6436630167aC498FE47B36fe8a9/contracts#address-tabs  
