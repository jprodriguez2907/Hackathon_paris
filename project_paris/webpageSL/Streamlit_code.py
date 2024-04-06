import streamlit as st
import os
import sys
from typer import Typer

st.set_page_config(layout="centered")
app = Typer()

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
CLI_path = os.path.join(grandparent_dir, "project_paris", "CLI")
image1_path = os.path.join(grandparent_dir, "img", "block1.png")
image2_path = os.path.join(grandparent_dir, "img", "block1.png")
sys.path.append(CLI_path)

st.set_option("deprecation.showPyplotGlobalUse", False)

def main():
    col1, col2, col3 = st.columns(3)

    with col3:
        st.write(" ")

    st.markdown(
        "<h1 style='text-align: center;'>Knowledge Nuggets Blockchain Quiz</h1>",
        unsafe_allow_html=True,
    )

    pages = [
        "Previous Knowledge",
        "Quiz 1",
        "Quiz 2",
        "Quiz 3",
        "Exchange",
    ]

    cols = st.columns(len(pages))

    total_correct_answers = st.session_state.get('total_correct_answers', 0)  # Obtener el contador guardado en la sesión

    for col, page in zip(cols, pages):
        if col.button(page):
            st.session_state.selected_page = page

    if "selected_page" not in st.session_state:
        st.image(image2_path, use_column_width=True)

    if "selected_page" in st.session_state:
        selected_page = st.session_state.selected_page

        if selected_page == "Previous Knowledge":
            st.markdown(
                """
                # Blockchain and Cryptocurrency Quiz Introduction

                Welcome to the Blockchain and Cryptocurrency Quiz! This quiz will challenge your understanding of key concepts related to blockchain technology and cryptocurrencies. Before you dive in, let's explore some fundamental concepts that will help you navigate the quiz effectively:

                ## Understanding Blockchain Technology:
                Blockchain technology is the foundation of cryptocurrencies and decentralized systems. At its core, a blockchain is a distributed ledger that records transactions in a secure and immutable manner. Unlike traditional centralized databases, which rely on a single authority to validate and store data, blockchains operate on a decentralized network of computers (nodes). Each transaction is encrypted and linked to the previous one, forming a chain of blocks. This decentralized architecture enhances transparency, security, and trust in the system.

                ## Exploring Cryptocurrencies:
                Cryptocurrencies are digital or virtual currencies that leverage cryptography for secure transactions and operate independently of central banks or governments. Bitcoin, introduced in 2009 by an anonymous person or group known as Satoshi Nakamoto, was the first cryptocurrency and remains the most well-known and widely used. Since then, thousands of other cryptocurrencies, often referred to as altcoins, have emerged, each with its unique features and use cases. Examples include Ethereum, Ripple, Litecoin, and many others.

                ## Unraveling Smart Contracts and Decentralized Applications (dApps):
                Smart contracts are self-executing contracts with the terms of the agreement directly written into code. They automatically execute and enforce the terms of a contract when predefined conditions are met, eliminating the need for intermediaries and enhancing efficiency and transparency. Decentralized applications (dApps) are applications that run on decentralized networks, such as blockchain, rather than a single central server. They offer various benefits, including censorship resistance, enhanced security, and greater user control over data and transactions.

                ## Diving into Consensus Mechanisms:
                Consensus mechanisms are protocols or algorithms used to achieve agreement among nodes in a distributed network on the validity of transactions or data. Proof of Work (PoW) and Proof of Stake (PoS) are two widely used consensus mechanisms in blockchain networks. PoW requires participants (miners) to solve complex mathematical puzzles to validate transactions and create new blocks, while PoS relies on participants (validators) holding a certain amount of cryptocurrency as collateral to validate transactions and secure the network. These consensus mechanisms play a crucial role in maintaining the integrity and security of blockchain networks.

                ## Additional Concepts to Explore:
                In addition to the core concepts mentioned above, the quiz will also cover topics such as tokens (digital assets or utilities on a blockchain), decentralized autonomous organizations (DAOs), private keys (cryptographic keys that provide access to cryptocurrencies), Merkle trees (data structures used to efficiently verify data in blockchain networks), and more.

                Now that you have a solid understanding of these fundamental concepts, you're ready to test your knowledge with the Blockchain and Cryptocurrency Quiz!
                """
            )

        elif selected_page == "Quiz 1":
            st.title("Quiz 1")
            total_correct_answers = run_quiz_1(total_correct_answers)

        elif selected_page == "Quiz 2":
            st.title("Quiz 2")
            total_correct_answers = run_quiz_2(total_correct_answers)

        elif selected_page == "Quiz 3":
            st.title("Quiz 3")
            total_correct_answers = run_quiz_3(total_correct_answers)

        elif selected_page == "Exchange":
            st.title("Exchange")
            total_correct_answers = exchange_points(total_correct_answers)

    st.session_state['total_correct_answers'] = total_correct_answers  # Guardar el contador en la sesión

def run_quiz_1(total_correct_answers):
    questions = [
        {
            "question": "What is a blockchain?",
            "options": ["A) A type of encryption algorithm",
                        "B) A centralized database",
                        "C) A decentralized, distributed ledger technology",
                        "D) A type of cryptocurrency"],
            "correct_answer": "C"
        },
        {
            "question": "What is Bitcoin?",
            "options": ["A) A physical coin",
                        "B) A digital cryptocurrency",
                        "C) A banking system",
                        "D) A type of stock"],
            "correct_answer": "B"
        },
        {
            "question": "What is a smart contract?",
            "options": ["A) A self-executing contract with the terms of the agreement directly written into code",
                        "B) A legal document",
                        "C) An insurance policy",
                        "D) A software bug"],
            "correct_answer": "A"
        },
        {
            "question": "What is a decentralized application (dApp)?",
            "options": ["A) A decentralized application that runs on a blockchain network",
                        "B) A mobile app",
                        "C) A centralized website",
                        "D) A type of cryptocurrency"],
            "correct_answer": "A"
        },
        {
            "question": "What is a consensus mechanism in blockchain?",
            "options": ["A) A type of digital signature",
                        "B) A type of encryption algorithm",
                        "C) A type of database",
                        "D) A mechanism used to achieve agreement on a single data value among distributed processes or systems"],
            "correct_answer": "D"
        }
    ]

    selected_options = []
    for i, q in enumerate(questions, start=1):
        st.write(f"**Question {i}:** {q['question']}")
        selected_option = st.radio("Select an option:",
                                   options=[f"{opt}" for opt in q['options']])
        selected_options.append(selected_option)

    if st.button("Check"):
        correct_answers = 0
        for i, q in enumerate(questions, start=1):
            if selected_options[i - 1].startswith(q['correct_answer']):
                correct_answers += 1

        st.write(f"You got {correct_answers} out of {len(questions)} questions correct.")
        if total_correct_answers is None:
            total_correct_answers = 0

        return total_correct_answers + correct_answers

def run_quiz_2(total_correct_answers):
    questions = [
        {
            "question": "What is Ethereum?",
            "options": ["A) A decentralized platform that enables smart contracts",
                        "B) A type of cryptocurrency",
                        "C) A physical coin",
                        "D) A centralized database"],
            "correct_answer": "B"
        },
        {
            "question": "What is a token in blockchain?",
            "options": ["A) A digital representation of an asset or utility on a blockchain",
                        "B) A type of encryption algorithm",
                        "C) A consensus mechanism",
                        "D) A type of cryptocurrency"],
            "correct_answer": "A"
        },
        {
            "question": "What is a DAO?",
            "options": ["A) A type of smart contract",
                        "B) A decentralized autonomous organization",
                        "C) A consensus mechanism",
                        "D) A type of cryptocurrency"],
            "correct_answer": "C"
        },
        {
            "question": "What is a private key?",
            "options": ["A) A secret number that allows bitcoins to be spent",
                        "B) A type of encryption algorithm",
                        "C) A consensus mechanism",
                        "D) A type of cryptocurrency"],
            "correct_answer": "B"
        },
        {
            "question": "What is a Merkle tree?",
            "options": ["A) A type of data structure used in blockchain",
                        "B) A type of consensus mechanism",
                        "C) A type of cryptocurrency",
                        "D) A type of encryption algorithm"],
            "correct_answer": "C"
        }
    ]

    selected_options = []
    for i, q in enumerate(questions, start=1):
        st.write(f"**Question {i}:** {q['question']}")
        selected_option = st.radio("Select an option:",
                                   options=[f"{opt}" for opt in q['options']])
        selected_options.append(selected_option)

    if st.button("Check"):
        correct_answers = 0
        for i, q in enumerate(questions, start=1):
            if selected_options[i - 1].startswith(q['correct_answer']):
                correct_answers += 1

        st.write(f"You got {correct_answers} out of {len(questions)} questions correct.")
        if total_correct_answers is None:
            total_correct_answers = 0

        return total_correct_answers + correct_answers

def run_quiz_3(total_correct_answers):
    questions = [
        {
            "question": "What is a Byzantine Fault?",
            "options": ["A) A type of encryption algorithm",
                        "B) A consensus mechanism in blockchain",
                        "C) A type of cryptocurrency",
                        "D) A smart contract vulnerability"],
            "correct_answer": "B"
        },
        {
            "question": "What does the term '51% attack' refer to?",
            "options": ["A) When a blockchain undergoes a hard fork",
                        "B) When a majority of nodes on a blockchain network collude to control over 51% of the network's mining power",
                        "C) When a smart contract fails to execute properly",
                        "D) When a cryptocurrency is delisted from exchanges"],
            "correct_answer": "B"
        },
        {
            "question": "What is the purpose of a nonce in mining?",
            "options": ["A) To add randomness to the mining process",
                        "B) To identify the miner's address",
                        "C) To encrypt transactions",
                        "D) To sign smart contracts"],
            "correct_answer": "A"
        },
        {
            "question": "What is the difference between proof of work and proof of stake?",
            "options": [
                "A) Proof of work requires miners to solve complex mathematical puzzles, while proof of stake requires validators to lock up a certain amount of cryptocurrency as collateral",
                "B) Proof of work relies on voting by coin holders, while proof of stake relies on computational power",
                "C) Proof of work is used in public blockchains, while proof of stake is used in private blockchains",
                "D) Proof of work is more energy efficient than proof of stake"],
            "correct_answer": "A"
        },
        {
            "question": "What is the 'halving' event in Bitcoin?",
            "options": ["A) The process of splitting a Bitcoin into smaller units",
                        "B) The periodical reduction in the rate at which new Bitcoin is created, occurring approximately every four years",
                        "C) The act of splitting the blockchain into two separate chains",
                        "D) The process of doubling the block size limit in Bitcoin"],
            "correct_answer": "B"
        }
    ]

    selected_options = []
    for i, q in enumerate(questions, start=1):
        st.write(f"**Question {i}:** {q['question']}")
        selected_option = st.radio("Select an option:",
                                   options=[f"{opt}" for opt in q['options']])
        selected_options.append(selected_option)

    if st.button("Check"):
        correct_answers = 0
        for i, q in enumerate(questions, start=1):
            if selected_options[i - 1].startswith(q['correct_answer']):
                correct_answers += 1

        st.write(f"You got {correct_answers} out of {len(questions)} questions correct.")
        if total_correct_answers is None:
            total_correct_answers = 0

        return total_correct_answers + correct_answers

def exchange_points(total_correct_answers):
    if total_correct_answers is None:
        total_correct_answers = 0
    else:
        total_correct_answers = total_correct_answers * 107

    st.write(f"Total cryptonuggets: {total_correct_answers}")

    st.subheader("Send cryptonuggets to another user")
    sender_private_key = st.text_input("Sender's Private Key:")
    recipient_public_key = st.text_input("Recipient's Public Key:")
    points_to_send = st.number_input("cryptonuggets to Send:", value=0, min_value=0, step=1)

    if st.button("Send"):
        if sender_private_key and recipient_public_key and points_to_send <= total_correct_answers:
            response = send_xrp(sender_private_key, points_to_send, recipient_public_key)
            st.write(response)
            total_correct_answers -= points_to_send
        elif not sender_private_key or not recipient_public_key:
            st.write("Please enter both sender's private key and recipient's public key.")
        else:
            st.write("Not enough points to send.")

    return total_correct_answers

def send_xrp(seed, amount, destination):
    import xrpl

    testnet_url = "https://s.altnet.rippletest.net:51234/"

    sending_wallet = xrpl.wallet.Wallet.from_seed(seed)
    client = xrpl.clients.JsonRpcClient(testnet_url)
    payment = xrpl.models.transactions.Payment(
        account=sending_wallet.address,
        amount=xrpl.utils.xrp_to_drops(int(amount)),
        destination=destination,
    )
    try:
        response = xrpl.transaction.submit_and_wait(payment, client, sending_wallet)
    except xrpl.transaction.XRPLReliableSubmissionException as e:
        response = f"Submit failed: {e}"
    return response

if __name__ == "__main__":
    main()
