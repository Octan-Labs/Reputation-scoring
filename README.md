# Octan Reputation Ranking System
Inspired by Google's PageRank, Octan Labs wants to build a similar system in Web3 space, namely Reputation Ranking System to helps
- Unify user data & reputation on multiple chains, then provides efficient metrics for new projects to target, acquire & incentivize potential users 
- Recognize all stakeholders, users & contributors by both staking & reputation weights, making DAOs more decentralized & democratic 
- Provide credit scoring to unleash under-collateral crypto lending.

Preliminary concepts:
- A node means an account (or public address) on a blockchain. It may be a personal account or a contract address.
- An edge indicates one or many directed transactions from account A to account B. 
- A (directed) graph consists of nodes and edges, presenting transactions among accounts.

Reputation Ranking System (RRS) typically computes reputation scores or ranking scores of all accounts in a certain graph.
Octan Labs defines three following schemas when computing reputation scores:
- *Global Reputation or Global Ranking* considers all acounts and transactions on a blockchain, for example, entirely on Ethereum (more than 200 million accounts and multi-billions of transactions between them since the genesis block). However, due to limitation in computing resources, we may restrict to most recently blocks within a deterministic timeframe, for instance, a range of all blocks from 00:00:01' Jan 1st, 2020 to 24:00:00' October 30st, 2022.   Global ranking score represents reputation or importance measurement of an account in the entire blockchain network.
- *Local/Category Reputation* considers subgraphs, i.e. sets of acounts and transactions filtered by specific (localized) criteria, for example, all transactions belonging to a token-contract (e.g. USDT), all accounts and transactions going throught Uniswap protocol or participating in DeFi markets. Local ranking score represents reputation or importance measurement of an account within a subspace of a blockchain network (currently, Octan consifers 5 subspace categories: DeFi, DAO, NFT, gamefi, socialfi).
- *Personalized/Project-based Reputation* computes reputation score of accounts relevant to one or many specific accounts, for example, a token-contract (e.g. USDT), to Uniswap protocol or to Axie Infinity game. Pertionalized ranking is similar to but not same as local ranking. It represents reputation or importance measurement of an account to one or many specific accounts.

All of reputation scores associated with a certain schema is normalized to 1000, i.e. sum of all reputation scores is 1000. 
