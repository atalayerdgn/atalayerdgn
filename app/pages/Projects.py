import streamlit as st


class Projects:
    def __init__(self) -> None:
        pass
    def Libft() -> None:
        """
        Libft Project Description
        """
        with st.expander("Libft"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to code a C library regrouping usual functions that you’ll be allowed to use in all your other projects.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("C")
                st.write("Makefile")
                st.write("Algorithms")
            with col2:
                st.write("Data Structures")
                st.write("Unit Tests")
                st.write("Makefile")
            st.markdown("-----")
    def ft_printf() -> None:
        """
        ft_printf Project Description
        """
        with st.expander("ft_printf"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to code a function that will mimic the real printf.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("C")
                st.write("Variadic Functions")
                st.write("Algorithms")
            with col2:
                st.write("Data Structures")
                st.write("Makefile")
            st.markdown("-----")
    def get_next_line() ->None:
        """
        get_next_line Project Description
        """
        with st.expander("get_next_line"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to code a function that returns a line ending with a newline, read from a file descriptor.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("C")
                st.write("File I/O")
                st.write("Algorithms")
            with col2:
                st.write("Data Structures")
                st.write("Makefile")
            st.markdown("-----")
    def Born2Beroot() -> None:
        """
        Born2Beroot Project Description
        """
        with st.expander("Born2Beroot"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to introduce you to the world of virtualization.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Virtualization")
                st.write("Linux")
                st.write("Security")
            with col2:
                st.write("Network")
                st.write("Firewall")
                st.write("Encryption")
            st.markdown("-----")
    def so_long() -> None:
        """
        so_long Project Description
        """
        with st.expander("So_Long"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to create a small 2D game.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("C")
                st.write("Minilibx")
                st.write("Algorithms")
            with col2:
                st.write("Data Structures")
                st.write("Makefile")
            st.markdown("-----")
    def pipex() -> None:
        """
        pipex Project Description
        """
        with st.expander("Pipex"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to code a program in which the execution of the following pipeline will be simulated.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("C")
                st.write("Linux System Programming")
                st.write("Algorithms")
            with col2:
                st.write("Data Structures")
                st.write("Unit Tests")
                st.write("Makefile")
            st.markdown("-----")
    def push_swap() -> None:
        """
        push_swap Project Description
        """
        with st.expander("Push_Swap"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to sort data on a stack, with a limited set of instructions, using the lowest possible number of actions.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("C")
                st.write("Makefile")
                st.write("Algorithms")
            with col2:
                st.write("Data Structures")
                st.write("Time Complexity")
                st.write("Makefile")
            st.markdown("-----")
    def Philosophers() -> None:
        """
        Philosophers Project Description
        """
        with st.expander("Philosophers"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to learn the basics of threading a process.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("C")
                st.write("Multi-Threading")
                st.write("Algorithms")
            with col2:
                st.write("Data Structures")
            st.markdown("-----")
    def Minishell() -> None:
        """
        Minishell Project Description
        """
        with st.expander("Minishell"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to create a simple shell.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("C")
                st.write("Linux System Programming")
                st.write("Algorithms")
            with col2:
                st.write("Data Structures")
                st.write("Architecture")
            st.markdown("-----")
    def cub3d() -> None:
        """
        Cub3D Project Description
        """
        with st.expander("Cub3D"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to create a dynamic view inside a maze.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("C")
                st.write("Minilibx")
                st.write("Algorithms")
            with col2:
                st.write("Data Structures")
                st.write("Raycasting")
            st.markdown("-----")
    def NetPractice() -> None:
        """
        NetPractice Project Description
        """
        with st.expander("NetPractice"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to learn the basics of network administration.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Network")
                st.write("Linux")
                st.write("Security")
            with col2:
                st.write("Firewall")
                st.write("Encryption")
                st.write("VPN")
            st.markdown("-----")
    def cpp_modules() -> None:
        """
        C++ Modules Project Description
        """
        with st.expander("C++ Modules"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to learn the basics of C++.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("C++")
                st.write("OOP")
                st.write("Algorithms")
                st.write("Inheritance")
                st.write("Error Handling")
            with col2:
                st.write("Data Structures")
                st.write("Polymorphism")
                st.write("STL Containers")
                st.write("Templates")
            st.markdown("-----")
    def Inception() -> None:
        """
        Inception Project Description
        """
        with st.expander("Inception"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is teaching you how to create a website using docker.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Docker")
                st.write("Web Server")
                st.write("SQL")
            with col2:
                st.write("Wordpress")
                st.write("Network")
                st.write("Security")
            st.markdown("-----")
    def PCA() -> None:
        with st.expander("PCA"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to learn the basics of Principal Component Analysis.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Machine Learning")
                st.write("Data Science")
                st.write("Data Processing")
            with col2:
                st.write("Data Visualization")
                st.write("Python")
                st.write("Jupyter Notebook")
            st.markdown("-----")
    def mean_and_covariance() -> None:
        """
        Mean and Covariance Project Description
        """
        with st.expander("Mean and Covariance"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to learn the basics of Mean and Covariance.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Machine Learning")
                st.write("Data Science")
                st.write("Data Processing")
            with col2:
                st.write("Data Visualization")
                st.write("Python")
                st.write("Jupyter Notebook")
            st.markdown("-----")
    def AI_For_Medicine() -> None:
        """
        AI For Medicine Project Description
        """
        with st.expander("Teknofest-AI For Medicine"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is detecting the disease from the X-ray images.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Machine Learning")
                st.write("Data Science")
                st.write("Data Processing")
            with col2:
                st.write("Data Visualization")
                st.write("Python")
                st.write("Image Processing")
            st.markdown("-----")
    def ft_irc() -> None:
        """
        ircserv with c++98 standarts
        """
        with st.expander("IRCserv"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to code an IRC server.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("C++98")
                st.write("Network")
                st.write("Algorithms")
            with col2:
                st.write("Data Structures")
                st.write("Makefile")
            st.markdown("-----")
    def computorv1() -> None:
        """
            Discriminant and Polynomial Roots with Python
        """
        with st.expander("ComputorV1"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to code a program that solves simple polynomial equations.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Python")
                st.write("Algorithms")
            with col2:
                st.write("Data Structures")
                st.write("Unit Tests")
                st.write("Makefile")
            st.markdown("-----")
    def ft_transcendence() -> None:
        """
        Creating Ping Pong game in web environment
        """
        with st.expander("ft_transcendence"):
            st.markdown("-----")
            st.subheader("Project Description")
            st.write("The aim of this project is to create a web-based multiplayer game.")
            st.subheader("Skills")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Docker")
                st.write("SQL")
                st.write("Microservices")
                st.write("JavaScript")
            with col2:
                st.write("Grafana and Prometheus")
                st.write("Blockchain")
                st.write("Python")
                st.write("Full Stack Development")
            st.markdown("-----")
    def Projects() -> None:
        """
        Projects Page
        """
        st.set_page_config(
        page_title="Projects",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded"
        )
        st.title("Projects")
        Projects.Libft()
        Projects.ft_printf()
        Projects.get_next_line()
        Projects.Born2Beroot()
        Projects.so_long()
        Projects.pipex()
        Projects.push_swap()
        Projects.Philosophers()
        Projects.Minishell()
        Projects.cub3d()
        Projects.NetPractice()
        Projects.cpp_modules()
        Projects.Inception()
        Projects.PCA()
        Projects.mean_and_covariance()
        Projects.AI_For_Medicine()
        Projects.ft_irc()
        Projects.computorv1()
        st.markdown("-----")
    
def main():
    Projects.Projects()

if __name__ == "__main__":
    main()
