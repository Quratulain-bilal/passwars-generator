import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np

# Inline CSS for background image and styling
st.markdown(
    """
    <style>
    /* Sidebar ko hide karein */
    section[data-testid="stSidebar"] {
        display: none;
    }

    /* Main content ko full width dein */
    section[data-testid="stMain"] {
        max-width: 100% !important;
        padding: 0 !important;
    }

    /* Body styling */
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://static.vecteezy.com/system/resources/thumbnails/006/217/670/small/closed-padlock-on-digital-background-cyber-security-vector.jpg') no-repeat center center fixed;
        background-size: cover;
    }

    /* Navbar Styling */
    .navbar {
        display: flex;
        justify-content: center;
        align-items: center;
        background: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(10px);
        padding: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        border-radius: 10px;
        margin: 10px auto;
        width: 90%;
        max-width: 1200px;
    }

    .navbar a {
        text-decoration: none;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
        transition: background 0.3s ease, transform 0.3s ease;
        margin: 0 10px;
    }

    .navbar a:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: scale(1.1);
    }

    /* Glassmorphism Effect for Containers */
    .glass {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 20px auto;
        width: 90%;
        max-width: 1200px;
    }

    /* Glowing Buttons */
    .stButton button {
        background: black; /* Black background */
        color: white; /* White text */
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
        transition: box-shadow 0.3s ease, transform 0.3s ease;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.7);
    }

    .stButton button:hover {
        box-shadow: 0 0 20px rgba(0, 0, 0, 1);
        transform: scale(1.05);
    }

    /* Title Styling */
    h1 {
        text-align: center;
        color: white;
        font-size: 3rem;
        margin-top: 20px;
        background: linear-gradient(135deg, #ffffff, #e0e0e0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.7);
    }

    /* Subtitle Styling */
    h3 {
        color: white;
        font-size: 1.5rem;
        margin-bottom: 10px;
        background: linear-gradient(135deg, #ffffff, #e0e0e0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.7);
    }

    /* Paragraph Styling */
    p {
        color: white;
        font-size: 1.1rem;
        line-height: 1.6;
        background: linear-gradient(135deg, #ffffff, #e0e0e0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.7);
    }

    /* Glass Background for Text Containers */
    .text-glass {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 20px auto;
        width: 90%;
        max-width: 1200px;
    }

    /* Mobile Responsiveness */
    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            padding: 5px;
        }

        .navbar a {
            margin: 5px 0;
            padding: 8px 16px;
        }

        h1 {
            font-size: 2rem;
        }

        h3 {
            font-size: 1.2rem;
        }

        p {
            font-size: 1rem;
        }

        .glass {
            padding: 15px;
            margin: 15px auto;
        }

        .stButton button {
            padding: 8px 16px;
            font-size: 14px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Navbar
st.markdown("""
<div class="navbar">
    <a href="/">Home</a>
    <a href="/Simple_Password">Simple Password</a>
    <a href="/Pattern_Password">Pattern Password</a>
    <a href="/Numeric_Password">Numeric Password</a>
    <a href="/Advanced_Password">Advanced Password</a>
    <a href="/Password_Tips">Password Tips</a>
</div>
""", unsafe_allow_html=True)

# Main Content
st.title("📱 Mobile Pattern Password Generator")

def generate_pattern_password():
    # Define the grid (3x3 grid for mobile pattern)
    grid = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    # Randomly select a pattern length (minimum 4 dots)
    pattern_length = random.randint(4, 9)

    # Start from a random point
    start_row = random.randint(0, 2)
    start_col = random.randint(0, 2)
    pattern = [grid[start_row][start_col]]

    # Generate the pattern
    for _ in range(pattern_length - 1):
        # Find possible moves
        possible_moves = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue  # Skip the current position
                new_row = start_row + dr
                new_col = start_col + dc
                if 0 <= new_row < 3 and 0 <= new_col < 3:
                    if grid[new_row][new_col] not in pattern:
                        possible_moves.append((new_row, new_col))

        # If no possible moves, break
        if not possible_moves:
            break

        # Randomly select a move
        start_row, start_col = random.choice(possible_moves)
        pattern.append(grid[start_row][start_col])

    return pattern

def plot_pattern(pattern):
    # Map pattern to coordinates
    coords = {
        "1": (0, 0), "2": (1, 0), "3": (2, 0),
        "4": (0, 1), "5": (1, 1), "6": (2, 1),
        "7": (0, 2), "8": (1, 2), "9": (2, 2),
    }

    # Extract x and y coordinates
    x = [coords[p][0] for p in pattern]
    y = [coords[p][1] for p in pattern]

    # Plot the grid
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_xlim(-0.5, 2.5)
    ax.set_ylim(-0.5, 2.5)
    ax.set_xticks([0, 1, 2])
    ax.set_yticks([0, 1, 2])
    ax.grid(True)

    # Plot the pattern
    ax.plot(x, y, marker="o", markersize=20, linestyle="-", color="blue", linewidth=3)

    # Hide axis labels
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    return fig

if st.button("Generate Mobile Pattern Password"):
    password = generate_pattern_password()
    st.markdown(f"""
    <div class="glass">
        <h3>Generated Password:</h3>
        <p style="font-size: 24px; font-weight: bold;">{"-".join(password)}</p>
    </div>
    """, unsafe_allow_html=True)

    # Display the pattern diagram
    st.write("### Pattern Diagram:")
    fig = plot_pattern(password)
    st.pyplot(fig)
