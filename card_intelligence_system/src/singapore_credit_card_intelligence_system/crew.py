import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	ScrapeWebsiteTool,
	FileReadTool
)





@CrewBase
class SingaporeCreditCardIntelligenceSystemCrew:
    """SingaporeCreditCardIntelligenceSystem crew"""

    
    @agent
    def singapore_credit_card_data_scraper(self) -> Agent:
        
        return Agent(
            config=self.agents_config["singapore_credit_card_data_scraper"],
            
            
            tools=[				ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
    
    @agent
    def credit_card_information_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["credit_card_information_analyst"],
            
            
            tools=[				FileReadTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
    
    @agent
    def credit_card_research_planner(self) -> Agent:
        
        return Agent(
            config=self.agents_config["credit_card_research_planner"],
            
            
            tools=[				ScrapeWebsiteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
    

    
    @task
    def plan_credit_card_data_sources(self) -> Task:
        return Task(
            config=self.tasks_config["plan_credit_card_data_sources"],
            markdown=False,
            
            
        )
    
    @task
    def scrape_credit_card_data(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_credit_card_data"],
            markdown=False,
            
            
        )
    
    @task
    def analyze_and_structure_card_information(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_and_structure_card_information"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the SingaporeCreditCardIntelligenceSystem crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


